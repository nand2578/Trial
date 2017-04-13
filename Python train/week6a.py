# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 07:45:51 2017

@author: anand005
"""

import urllib

url = 'http://python-data.dr-chuck.net/comments_42.json'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
print data

import json

info = json.loads(data)
print 'Name count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Count', item['count']