# -*- coding: utf-8 -*-


import requests
import time
import random
import string
from apisms import _5sim, onlinesim
from . import ProxyManager
from python3_anticaptcha import ImageToTextTask
from lxml import html, etree


def rsleep(left = 2, right = 5):
    time.sleep(random.triangular(left, right))

def prepare():
    pm = ProxyManager.ProxyMN()
    proxy = {'https': 'http://' + pm.GetProxyList(Limit = 1, Type = 'https')[0] + '/'}
    http = requests.Session()
    http.headers.update({
                'User-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; XT1022 Build/KXC21.5-40) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30'
            })
    http.proxies = proxy
    resp = http.get('https://m.vk.com/')
    return http, resp

def start(session, name, surname, year, month, day, sex, captcha_sid = None, captcha_key = None):
    url = "https://m.vk.com/join.php?act=start"
    values = {'act': 'start',
              'first_name': name,
              'last_name': surname,
              'bday': day,
              'bmonth': month,
              'byear': year,
              'sex': sex,
              '_nlm': '1',
              '_ref': 'join'
              }
    if captcha_sid is not None:
        values['captcha_sid'] = captcha_sid
        values['captcha_key'] = captcha_key
    
    response = session.post(url, values)
    return session, response


def get_sms(session, phone_number, _hash):
    values = {'act': 'phone',
              'hash': _hash,
              '_nlm': '1',
              '_ref': 'join'
              }
    if phone_number.startswith('+77'):
        values['phone_prefix'] = '+77'
        values['phone_number'] = phone_number.split('+77')[1]
    elif phone_number.startswith('+7'):
        values['phone_prefix'] = '+7'
        values['phone_number'] = phone_number.split('+7')[1]
    
    url = "https://m.vk.com/join?act=phone&hash=" + _hash
    response = session.post(url, values)
    return session, response
    

def check_code(session, phone_number, code, _hash):
    url = "https://m.vk.com/join?act=check_code&hash=" + _hash
    values = {'act': 'check_code',
              'hash': _hash,
              'phone': phone_number,
              'code': code,
              '_nlm': '1',
              '_ref': 'join'
              }
    response = session.post(url, values)
    return session, response

def finish(session, key_url, phone_number, password):#session, phone_number, password, key_url):
    """a = key_url.split('?')[1]
    values = {}
    for i in a.split('&'):
        b = i.split('=')
        values[b[0]] = b[1]
    for i, j in values.items():
        print(i, j)
        
    values = {
              
              'expire': '',
              'recaptcha': '',
              'captcha_sid': '',
              'captcha_key': '',
              'email': phone_number,
              'pass': password,
              'join_to_already': 0
              }"""
    values = {'email': phone_number,
              'pass': password
              }
    key_url = key_url[:4] + key_url[5:]
    response = session.post(key_url, values)
    return session, response
    
    
    
#finish("https://login.vk.com/?act=login&_origin=https://m.vk.com&ip_h=338750eb054fc82b33&lg_h=bb495da8821fd6e060&role=pda&join_code=12654&join_hash=724ec96c1c2412ec10b45c0be0cb644c&to=am9pbj9hY3Q9ZG9uZQ--&pass=dima_bog_debaga")


def registration(name = 'Лада', surname = 'Беленова', sex = '1', birthday = None, country = 'kazakhstan', service = '5sim'):
    try:
        session, response = prepare()
        
        rsleep()
        
        if birthday is None:
            byear = str(random.randint(1980, 1998))
            bmonth = str(random.randint(1, 12))
            bday = str(random.randint(1, 28))
        else:
            bday, bmonth, byear = birthday.split('.')
            
        session, response = start(session, name, surname, byear, bmonth, bday, sex)
        while 'captcha' in response.text:
            print('we need captcha')
            pm = ProxyManager.ProxyMN()
            prxlst = pm.GetProxyList(Limit = 5, Type = 'https')
            for i in range(5):
                try:
                    proxy = {'https': 'http://' + prxlst[i] + '/'}
                    session.proxies = proxy
                    session, response = start(session, name, surname, byear, bmonth, bday, sex)
                    if 'captcha' not in response.text:
                        break
                except Exception:
                    print('problems')
            
        print(response.text)
        _hash = response.text.split('action="/join?act=phone&hash=')[1].split('"')[0]
        print('gonna get phone')
        
    
            
    
        
        if service == '5sim':
            ss = _5sim._5simApi()
            
        elif service == 'onlinesim':
            ss = onlinesim.onlinesimApi()
        
        phone_number =  ss.get_number(country = country) 
        print('number has been got', phone_number) 
        session, response = get_sms(session, phone_number, _hash)
        print(response.text)
        sms_code = None
        i = 0
        while sms_code is None:
            time.sleep(1)
            i += 1
            sms_code = ss.check()
            print(sms_code)
            if i >= 60:
                print('no sms')
                ss.ban()
                return registration(name, surname, sex, birthday, country, service)
        session, response = check_code(session, phone_number, sms_code, _hash)
        print(response.text)
        key_url = response.text.split('<form method="post" action="')[1].split('"')[0]
        print(key_url)
        password = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=12))
        session, response = finish(session, key_url, phone_number, password)
        print(response.text)
        return [phone_number, password]
    except Exception:
        return registration(name, surname, sex, birthday, country, service)




