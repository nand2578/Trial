# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:49:42 2016

@author: anand005
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.data.pr4e.org', 80))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

#http://data.pr4e.org/intro-short.txt