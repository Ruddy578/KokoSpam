import vk_api, time
from vk_api import upload


class Bot():
    
    def __init__(self, login = None, password = None, vk = None):
        if vk:
            self.vk = vk
            self.vk.auth()
        elif login and password:
            self.vk = vk_api.VkApi(login = login, password = password)
            self.vk.auth()
        else:
            print('something wrong', login, password, vk)
            raise Exception
        self.uid = vk.method('users.get')[0]['id']
        self.vku = upload.VkUpload(self.vk)
        
        
    def joinGroup(self, groupId):
        try:
            self.vk.method('groups.join', {'group_id': groupId})
            return 1
        except Exception:
            return 0
    
    def like(self, item_id, _type):
        try:
            self.vk.method('likes.add', {'item_id': item_id, 'type': _type})
            return 1
        except Exception:
            return 0
        
    
    def addFriend(self, fr_id):
        try:
            self.vk.method('friends.add', {'user_id': fr_id})
            return 1
        except Exception:
            return 0
        
    
    def makeRepost(self, _object, message = None):
        try:
            if message:
                self.vk.method('wall.repost', {'object': _object, 'message': message})
            else:
                self.vk.method('wall.repost', {'object': _object})
            return 1
        except Exception:
            return 0
    
    def makePost(self, owner_id = self.uid, message =  None, attachments = '', photos = None):
        if message is None and attachments == '' and photos is None:
            print('message and attachments cant be None')
        if photos is not None:
            resp = self.vku.photo_wall(photos)
            for i in resp.json():
                attachments += 'photo' + i['owner_id'] + '_' + i['id'] + ','
        values = {'owner_id': owner_id,
                  'message': message,
                  'attachments': attachments}
        return self.vk.method('wall.post', values)
    
    def sendMessage(target_id, text = None, attachment = None, forward_messages = None, sticker_id = None):
        values = {'user_id': target_id}
        if text:
            values['message'] = text
        if attachment:
            values['attachment'] = attachment
        if forward_messages:
            values['forward_messages'] = forward_messages
        if sticker_id:
            values['sticker_id'] = sticker_id
        return self.vk.method('messages.send', values)
    
    def getPosts(owner_id = None, domain = None, count = 20, extended = 0, filter = 'all'):
        values = {}
        if owner_id:
            values['owner_id'] = owner_id
        if domain:
            values['domain'] = domain
        values['count'] = count
        values['extended'] = extended
        values['filter'] = filter
        return self.vk.method('wall.get', values)
    
    def updateBaseInfo(maiden_name = None, screen_name = None, sex = None, relation = None, relation_partner_id = None, bdate = None, bdate_visibility = None, home_town = None, country_id = None, city_id = None, status = None):
        values = {}
	if maiden_name:
		values["maiden_name"] = maiden_name
	if screen_name:
		values["screen_name"] = screen_name
	if cancel_request_id:
		values["cancel_request_id"] = cancel_request_id
	if sex:
		values["sex"] = sex
	if relation:
		values["relation"] = relation
	if relation_partner_id:
		values["relation_partner_id"] = relation_partner_id
	if bdate:
		values["bdate"] = bdate
	if bdate_visibility:
		values["bdate_visibility"] = bdate_visibility
	if home_town:
		values["home_town"] = home_town
	if country_id:
		values["country_id"] = country_id
	if city_id:
		values["city_id"] = city_id
	if status:
		values["status"] = status
	return self.vk.method("account.saveProfileInfo", values)
    
        