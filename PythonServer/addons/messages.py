# -*- coding: utf-8 -*-


import vk_api 
import requests, time
from vk_api import upload


def getDialogs(vk, unread = 0):
    return vk.method('getDialogs')

def write_msg(vk, user_id, msg = None, photos = None, sticker_id = None):
    values = {}
    if not ( msg or photos or sticker_id):
        raise Exception
    if msg:
        values['message'] = msg
    attachments = ''
    if photos:
        for photo in photos:
            resp = upload.photo_messages(photo)
            attachments += 'photo' + resp.json()['owner_id'] + '_' + resp.json()['id'] + ','
    values['attachments'] = attachments
    if sticker_id:
        values['sticker_id'] = sticker_id
    values['user_id'] = user_id
    return vk.method('messages.send', values)





def spam(vks, user_id, msg = None, photos = None, sticker_id = None):
    for vk in vks:
        write_msg(vk, user_id, msg, photos, sticker_id)
            
                
            