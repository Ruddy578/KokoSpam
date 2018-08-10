#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
# Turn on debug mode.

import pymysql.cursors

# Подключиться к базе данных.


class Database():
    
    def __init__(self,
                 host = 'mysql70.hostland.ru',
                 user = 'host1677485', 
                 password = 'zZoQNHGf',
                 db = 'host1677485',
                 table = None):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.connection = pymysql.connect(host = self.host,
                                     user = self.user,
                                     password = self.password,
                                     db = self.db,
                                     charset = 'utf8',
                                     autocommit = True)
        self.table = table
    
    def execute(self, sqlcommand):
        with self.connection.cursor() as cursor:
            cursor.execute(sqlcommand)
            #self.connection.close()   
            return cursor
    
    def get(self, name, condition):  
        ans = []
        qq = 'SELECT ' + name + ' FROM ' + self.table + ' WHERE ' + condition
        #print(qq)
        cursor = self.execute(qq)
        
        for row in cursor:
                ans.append(row)

        return ans
    
    def set(self, key, keyvalue, param, paramvalue):   
        qq = 'UPDATE `' + self.table + '` SET `' + param + '` = ' + paramvalue +   ' WHERE `' + self.table + '`.`'+ key + '` = ' + keyvalue
        return self.execute( qq)

    
    def delete(self, param, paramvalue):
        return self.execute('DELETE FROM ' + self.table + ' WHERE ' + param + ' = ' + paramvalue)
    
    def add(self, values):
        qq ="INSERT INTO `" + self.table +"` "+ str(tuple(values.keys())).replace("'", "`") + " VALUES " + str(tuple(values.values())).replace("'NULL'", "NULL") + ';'
        
        return self.execute(qq )
    
    def close(self):
        self.connection.close()
        

#proxy = Database(table = 'Proxy')
#proxy.get('Proxy', '*', 'id = 1')
#proxy.add('Proxy', {'id': 'NULL', 'ip' : '1222333', 'port' : '1222', 'login': 'ddddd', 'password': 'qwerty', 'ltimeuse': '122333'})
#proxy.delete('Proxy', 'id', '2')
#proxy.set('id', '7', 'type', "'ssl'")
#proxy.add( {'id': 'NULL', 'ip' : '1222333', 'port' : '1222', 'login': 'ddddd', 'password': 'qwerty', 'ltimeuse': '10', 'type': 'https'})
#proxy.add( {'ip' : '1222333', 'port' : '1222', 'login': 'ddddd', 'password': 'qwerty', 'ltimeuse': '130', 'type': 'https'})

#a = proxy.get('MAX(ltimeuse)', "type = 'https'")
#print(a)
#b = proxy.get('*', "type = 'https' AND ltimeuse = '" + str(a[0][0]) + "'")
#print(b)