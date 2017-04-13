# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 07:45:51 2017

@author: anand005
"""

import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_314695.json'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

info = json.loads(data)
#print 'Name count:', len(info)
names_list = info.values()[1]
print 'Name count:', len(names_list)

#for i in names_list:
 #   print i['name']
  #  print i['count']

sum = 0    
for item in names_list:
    sum = sum + item.values()[0]
    
print 'SUM:', sum