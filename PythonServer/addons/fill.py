 # -*- coding: utf-8 -*-

import requests, vk_api
import random
import os


def to_normal_str(a):
    a = a.split("'")[1::2]
    ans = ''
    for i in  a:
        if i != ', ':
            ans += i + ', '
    if len(ans) > 2:
        return ans[:-2]
    else:
        return 'Pushkin'

def from_file(path):
    f = open(path)
    a = to_normal_str(random.choice(f.readlines()))
    f.close()        
    return a

class filler(object):
    
    
    def __init__(self, vk = None, login = None, password = None):
        if vk is None:
            self.vk = vk_api.VkApi(login = login, password = password)
            self.vk.auth()
        else:
            self.vk = vk
        
    

    
    
    def fill_interests(self, values = None):
        example = {'about': from_file(u'database/О себе.txt'), 
                         'activities': from_file('database/Деятельность.txt'),
                         'books': from_file('database/Любимые книги.txt'),
                         'games': from_file('database/Любимые игры.txt'),
                         'interests': from_file('database/Интересы.txt'),
                         'movies': from_file('database/Любимые фильмы.txt'),
                         'music': from_file('database/Любимая музыка.txt'),
                         'quotes': from_file('database/Любимые цитаты.txt'),
                         'tv': from_file('database/Любимые телешоу.txt')
                         }
        if values is None:
            values = example
        else:
            for i in example.keys():
                if i not in values.keys():
                    values[i] = example[i]
                    
        self.vk.set_interests(values)
    
    
    def fill_life_position(self, values = None):
        
        example = {'alcohol': random.randint(1, 5), 
                         'inspired_by': from_file('database/Вдохновляют.txt'),
                         'life_priority': random.randint(1, 8), 
                         'people_priority': random.randint(1, 6),
                         'political': random.randint(1, 8),
                         'religion': random.choice([167, 102, 101, 107, 124, 129, 139, 200, 201]), 
                         'religion_custom': '',
                         'smoking': random.randint(1, 5)
                         }
        
        if values is None:
            values = example
        else:
            for i in example.keys():
                if i not in values.keys():
                    values[i] = example[i]
        self.vk.set_life_position(values)
    
    
    def fill_main_photo(self, path = 'random_photos/' + random.choice(os.listdir('addons/random_photos'))):
        a = self.vk.method("photos.getOwnerPhotoUploadServer")
        b = requests.post(a['upload_url'], files = {'photo': open(path, 'rb')}).json()   
        c = self.vk.method('photos.saveOwnerPhoto', {"server": b['server'], 'hash': b['hash'], 'photo': b['photo']})
        print(c)
        return c        
        

#fil = filler(login = "+7 (910) 482-2951", password = 'IywKIkVc')


