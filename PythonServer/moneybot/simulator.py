import vk_api, bot
import time, random
import fill
import scrapper


def load_accounts(path):
    f  = open(path)
    ans = []
    for line in f:
        try:
            a = line.strip().split(':')
            vk = vk_api.VkApi(login = a[0], password = a[1])
            vk.auth()
            ans.append(vk, a[2])
        except Exception:
            print('it does not work')
    return ans

class Simulator():
    def __init__(self, login = None, password = None, vk = None):
        if vk:
            self.vk = vk
            self.bot = bot.Bot(vk)
            self.vk.auth()
        elif login and password:
            self.vk = vk_api.VkApi(login = login, password = password)
            self.bot = bot.Bot(self.vk)
            self.vk.auth()
        else:
            print('something wrong', login, password, vk)
            raise Exception
        
        self.accounts = load_accounts('accounts.txt')
        

    
    