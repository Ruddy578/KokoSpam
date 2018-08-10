import requests
from lxml import html, etree

method_url = input()
response = requests.get(method_url)
#print(response.text)
tree = html.fromstring(response.text)
info = tree.xpath('//td[@class="dev_param_name"]/text()')
values = {}
for i in info:
    if i[0] not in '1234567890':
        values[i] = 'None'
#print(values)
ans = 'def method('
i = 0
for key, value in values.items():
    ans += key + ' = ' + value
    if i < len(values) - 1:
        ans += ', '
    i += 1
ans += '):\n'
ans += '\tvalues = {}\n'
for key, value in values.items():
    ans += '\tif ' + key + ':\n' + '\t\tvalues["' + key + '"] = ' + key + '\n'
methodname = tree.xpath('//*[@id="dev_page_cont"]/div[1]/div[2]/div[1]/span[2]/text()')[0]
#print(methodname)
ans += '\treturn self.vk.method("' + methodname + '", values)'
print(ans)














"""import ProxyManager
import requests
from python3_anticaptcha import ImageToTextTask

proxy = {'https': 'http://' + pm.GetProxyList(Limit = 1, Type = 'https')[0] + '/'}
http = requests.Session()
http.headers.update({
            'User-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.4; en-US; XT1022 Build/KXC21.5-40) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.7.0.636 U3/0.8.0 Mobile Safari/534.30'
        })
http.proxies = proxy

values =  {'act': 'start',
              'first_name': '≈гор',
              'last_name': '÷арь',
              'bday': '6',
              'bmonth': '3',
              'byear': '1988',
              'sex': '1',
              '_nlm': '1',
              '_ref': 'join'
              }
response = http.post('https://m.vk.com/join?act=start', values)
print(response.text)
i = 0
while 'captcha' in response.text:
    print(i)
    i += 1
    captcha_sid = response.text.split('<input type="hidden" name="captcha_sid" value="')[1].split('"')[0]
    print('captcha_sid:', captcha_sid)
    captcha_url = 'https://m.vk.com/captcha.php?sid=' + captcha_sid
    captcha_key = ImageToTextTask.ImageToTextTask(anticaptcha_key='bef684c06ed5ba09377e714b4bb2f5b2', save_format='const').captcha_handler(captcha_link = captcha_url)['solution']['text']
    print('captcha_key:', captcha_key)
    values['captcha_sid'] = captcha_sid
    values['captcha_key'] = captcha_key
    response = http.post('https://m.vk.com/join.php?act=start', values)
print(response.text)
values = {'email': '+77052192203', 
          'pass': 'QWErty132'}
resp = requests.post('http://login.vk.com/?act=login&_origin=https://m.vk.com&ip_h=21731493212eb6b020&lg_h=1ebeda4f0d42459220&role=pda&join_code=42197&join_hash=9c93c5e0e7ddedcdee122e0553f8fe8d&to=am9pbj9hY3Q9ZG9uZQ--', values)
print(resp.text)"""