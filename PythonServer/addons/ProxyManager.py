#from . import dbconnect
import requests
import time
def CheckProxy( ProxyList, SiteUrl = 'https://m.vk.com', TimeOut = 5, Type = 'https'):
    ans = []
    for proxy in ProxyList:
        try:
            proxytemplate = {
                Type: 'http://' + proxy + '/',
            }
            yourreq = requests.Session()
            yourreq.headers.update({
                        'User-agent': 'Mozilla/5.0 (Windows NT 6.1; rv:52.0) '
                                        'Gecko/20100101 Firefox/57.0'
                    })
            yourreq.proxies = proxytemplate
            r = yourreq.get(SiteUrl, timeout = TimeOut)
            ans.append(proxy)
        except Exception:
            pass
    return ans




class ProxyMN():
    
    
    def __init__(self):
        self.key = "037967f9be5b7bdb651b6f9126af4218"
    #type: http, https, ...
    
    def GetProxyList(self, Type = 'https', Anonymity = '2', Response = 300, Limit = 0):

        
        
       
        url = 'http://api.best-proxies.ru/proxylist.txt?key=' + self.key +'&speed=1&type=' + Type + '&response=' + str(Response) + '&limit=0'  + '&level=' + Anonymity
        proxies = requests.get(url).text.split()
        #print(proxies)
        if Limit == 0:
            ans = CheckProxy(proxies, Type = Type)
        else:
            i = 0
            ans = []
            while len(ans) < Limit and i < len(proxies):
                print(proxies[i])
                a = CheckProxy([proxies[i]], Type = Type)
                if len(a) == 1:
                    ans.append(a[0])
                i += 1
        return ans
    
class ProxyMNDB():
    
    def __init__(self):
        self.proxyDB = dbconnect.Database(table = 'Proxy')
    
    def AddProxy(self, ProxyList):
        #proxy - словарь с ключами - названиями столбцов в БД, значениями - со значениями столбцов в БД
        for proxy in ProxyList:
            self.proxyDB.add(proxy)

    
    def DelProxy(self, ProxyList):
        for proxy in ProxyList:
            self.proxyDB.delete('ip',"'" + proxy['ip'] + "'")
    
    def GetProxy(self, Type = 'https'):
        #SELECT * FROM Proxy WHERE ltimeuse = (SELECT MIN(ltimeuse) FROM Proxy)

        proxy = self.proxyDB.get('*', "type = '" + Type + "' AND ltimeuse = (SELECT MIN(ltimeuse) FROM Proxy)")
        return proxy
    
    def UpdateProxy(self, proxy):
        for key, value in proxy.items():
            print(key, value)
            self.proxyDB.set('id', proxy['id'], key, value)
            
    def close(self):
        self.proxyDB.close()
    
    def unpack(self, proxies_from_db):
        ans = []
        for proxy in proxies_from_db:
            ans.append({proxy[6]: proxy[6] + "://" + proxy[3] + ':' + proxy[4] + '@' + proxy[1] + ':' + str(proxy[2])})
        return ans
    
    def pack(self, proxies_to_db):
        #{"https": "https://YjmyXh:zHHu6a@36.0.198.114:8000/"} -> {'id': 'NULL', 'ip' : '36.0.198.114', 'port' : '8000', 'login': 'YjmyXh', 'password': 'zHHu6a', 'type': 'https'}
        ans = []
        for proxy in proxies_to_db:
            pass
        

proxy =  [{'id': 'NULL', 'ip' : '53.165.98.114', 'port' : '8080', 'login': 'user', 'password': 'passw', 'type': 'socks4'},{'id': 'NULL', 'ip' : '53.165.98.114', 'port' : '8080', 'login': 'user', 'password': 'passw', 'type': 'socks5'},{'id': 'NULL', 'ip' : '53.165.98.114', 'port' : '8080', 'login': 'user', 'password': 'passw', 'type': 'http'},{'id': 'NULL', 'ip' : '53.165.98.114', 'port' : '8080', 'login': 'user', 'password': 'passw', 'type': 'socks5'}] 
#pdb = ProxyMNDB()
#newproxy = {'id': '7', 'ip' : "'53.165.98.114'", 'port' : '8000', 'login': "'user'", 'password': "'passw'", 'type': "'https'", 'ltimeuse': '40'}
#print(pdb.unpack(pdb.GetProxy(Type = "socks4")))
#pdb.AddProxy(proxy)
#pdb.DelProxy([proxy[0]])
#pdb.close()

#pm = ProxyMN()
#print(pm.GetProxyList(Limit = 1, Type = 'https'))
