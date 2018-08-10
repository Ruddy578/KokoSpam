# -*- coding: utf-8 -*-

import vk_api
from lxml import html, etree
import time


def parse(url = 'https://vk.com/hinser'):
    ans = {}
    text = vk.get_data(url)
    tree = html.fromstring(text)
    info = tree.xpath('.//div[@class = "clear_fix profile_info_row "]') + tree.xpath('.//div[@class = "clear_fix profile_info_row block"]')
    for i in info:
        tt = i.xpath('./div[1]/text()') + i.xpath('./div[1]/a/text()')
        #print(tt)
        tt2 = i.xpath('./div[2]/a/text()') + i.xpath('./div[2]/text()')
        #print(tt2)
        if len(tt) > 0 and len(tt2) > 0:
            ans[tt[0]] = tt2
    if len(tree.xpath('.//h2[@class = "page_name"]/text()')) > 0:
        ans['Имя:'] = tree.xpath('.//h2[@class = "page_name"]/text()')[0]
    if len(tree.xpath('.//span[@class = "current_text"]/text()')) > 0:
        ans['Статус:'] = tree.xpath('.//span[@class = "current_text"]/text()')[0]    
    print(ans)
    return ans
    
    
vk = vk_api.VkApi(login = '+79165684716', password = 'QWErty132')
vk.auth()
def write_data():
    
    for j in range(89850001, 89851000):
        dd = parse(url = 'https://vk.com/id' + str(j))
        logs = open('logs.txt', 'a')
        try:
            print(dd, file = logs)
        except Exception:
            pass
        logs.close()
        for i in dd.keys():
            
            fout = open('database/' + i[:-1].replace('/', '') + '.txt', 'a')
            try:
                print(str(dd[i]), file = fout)
            except Exception:
                print('Капец человек даун такие символы использовать, да пошёл он..')
            fout.close()
        time.sleep(3)
        logs.close()
        
        
def get_users():
    text = vk.get_search_rezult({'c[group]': 30602036, 'offset':140})
    print(text)
    time.sleep(1)
    tree = html.fromstring(text)
    users = tree.xpath('.//div[@class = "labeled name"]/a[1]/@href')
    print(users)

write_data()
print('done')
