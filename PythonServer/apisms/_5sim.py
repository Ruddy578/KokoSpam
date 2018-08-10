import requests, json
import time 

#contries: russia, kazakhstan

class _5simApi(object):
    
    
    def __init__(self):
        self.http = requests.Session()
        self.http.headers.update({
            'Authorization': 'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTY5Njg4NzUsImlhdCI6MTUyNTQzMjg3NSwicmF5IjoiNzYxNmI0NTQwMWZlMWRkMDk5M2Y4YmNlZGVkODg2YjgiLCJzdWIiOjU1MDM4fQ.ucFQNQ13VZ9JoNXVX9nVLRMkmomgWnm4K8rIQdqJOMfO_u00_dzTJ-tWv0OiajybSMCWqagZ-QbUKWxvx8vLFqi57AAJvAGw_U1cXmk1syFHcYgEgE2LUMx821j6qoldX70478RgmqjJ9qNIZUb-h1IROgVqhwsYPVqtyOxd1YMIE1lZ1thDbvuXHLBIL31aHQYnA3rDWPK7CsogQLBvPaNWfjTYRphxrXCaUNAHZ6xMBWIIsd2qhqp_EhjTHewgWmRfnf9BqD-0Jt1dJwXMmop-0zA1AupDZJmR7I79S7g-VRQP-GFrYtknJSGGcxzRCaDMi1T1AN6gZdAjq_c-GA'
            
        })  
        #eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTY5Njg4NzUsImlhdCI6MTUyNTQzMjg3NSwicmF5IjoiNzYxNmI0NTQwMWZlMWRkMDk5M2Y4YmNlZGVkODg2YjgiLCJzdWIiOjU1MDM4fQ.ucFQNQ13VZ9JoNXVX9nVLRMkmomgWnm4K8rIQdqJOMfO_u00_dzTJ-tWv0OiajybSMCWqagZ-QbUKWxvx8vLFqi57AAJvAGw_U1cXmk1syFHcYgEgE2LUMx821j6qoldX70478RgmqjJ9qNIZUb-h1IROgVqhwsYPVqtyOxd1YMIE1lZ1thDbvuXHLBIL31aHQYnA3rDWPK7CsogQLBvPaNWfjTYRphxrXCaUNAHZ6xMBWIIsd2qhqp_EhjTHewgWmRfnf9BqD-0Jt1dJwXMmop-0zA1AupDZJmR7I79S7g-VRQP-GFrYtknJSGGcxzRCaDMi1T1AN6gZdAjq_c-GA
        self.tzid = None
        self.phone_number = None
       
        
    def get_balance(self):
        resp = self.http.get('https://5sim.net/v1/user/profile')
        return resp.json()['balance']
    
    def get_info_of_numbers(self):
        resp1 = self.http.get('https://5sim.net/v1/guest/products/russia/any')
        rus = resp1.json()['vkontakte']
        resp1 = self.http.get('https://5sim.net/v1/guest/products/kazakhstan/any')
        kaz = resp1.json()['vkontakte'] 
        ans = {'rus': {'amount': rus['Qty'], 'price': rus['Price']},
               'kaz': {'amount': kaz['Qty'], 'price': kaz['Price']}
               }
        return ans
    
    def get_number(self, country = 'kazakhstan'):
        resp = self.http.get('https://5sim.net/v1/user/buy/activation/'+country+'/any/vkontakte')
        print(resp)
        if resp.ok:
            print(resp.json())
            print(resp.json()['phone'])
            self.tzid = resp.json()['id']
            self.phone_number = resp.json()['phone']
            return self.phone_number
        else:
            return self.get_number(country)
    
    def check(self):
        resp = self.http.get('https://5sim.net/v1/user/check/'+str(self.tzid))
        print(resp.json())
        
        if resp.json()['sms'] == []: 
            return None
        return resp.json()['sms'][0]['code']
    
    def ban(self):
        resp = self.http.get('https://5sim.net/v1/user/ban/' + str(self.tzid))
        print(resp)
        return resp
    
    def finish(self):
        resp = self.http.get('https://5sim.net/v1/user/finish/' + str(self.tzid))
        print(resp)
        return resp
#ss = _5simApi()
#print(ss.get_info_of_numbers())