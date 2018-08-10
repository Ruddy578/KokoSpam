


import requests, json
import time 


#contries: 7 - russia



def get_phone(apikey):
    tzid = -1
    r = requests.get("http://onlinesim.ru/api/getNum.php?apikey=" + apikey + "&country=7&service=VKcom")
    if r.json()['response'] == 1:
        tzid = r.json()['tzid']
    else:
        print("sorry boys", r.json()['response'])
    return tzid



class onlinesimApi(object):
    
    
    def __init__(self, api_key ="9b6d760fa5e3137d3d826d9859b4fb5b" ):
        self.http = requests.Session()
        self.api_key = api_key
        self.tzid = None
        self.phone_number = None
       
        
    def get_balance(self):
        resp = self.http.get("http://onlinesim.ru/api/getBalance.php?apikey=" + self.api_key)
        return resp.json()['balance']
    
    def get_info_of_numbers(self):
        resp1 = self.http.get("http://onlinesim.ru/api/getServiceList.php?country=7&apikey=" + self.api_key)
        a = resp1.json()['0']
        ans = {'rus' : {'amount': a['limit'], 'price': a['index']}
               }
        return ans
    
    def get_number(self, country = 7):
        tzid = get_phone(self.api_key)
        print(tzid)
        if tzid == -1:
            print("sorry boys, something goes wrong")
            return None
        else:
            self.tzid = tzid
            time.sleep(10)
            r = requests.get("http://onlinesim.ru/api/getState.php?apikey=" + self.api_key + "&message_to_code=1&tzid=" + str(tzid))
            print(r.json())
            while 'number' not in r.json()[0]:
                time.sleep(10)
                r = requests.get("http://onlinesim.ru/api/getState.php?apikey=" + self.api_key + "&message_to_code=1&tzid=" + str(tzid))
                print(r.json())
            self.phone_number = r.json()[0]['number']
            
        return  self.phone_number
    
    def check(self):
        r = requests.get("http://onlinesim.ru/api/getState.php?apikey=" + self.api_key + "&message_to_code=1&tzid=" + str(self.tzid))
        if r.json()[0]['response'] == 'TZ_NUM_ANSWER':
            return r.json()[0]['msg']
        return r.json()
    
    def ban(self):
        pass
    
    def finish(self):
        pass

#ss = onlinesimApi()
#print(ss.get_balance())
#print(ss.get_info_of_numbers())