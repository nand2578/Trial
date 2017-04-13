import urllib
from bs4 import BeautifulSoup

counts = raw_input('Enter Count')
pos = raw_input('Enter Position')

url = 'http://python-data.dr-chuck.net/known_by_Tamta.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

count =0
while count < int(counts):
    url = tags[int(pos)-1].get('href',None)
    content = tags[int(pos)-1].contents[0]
    print content
    count = count +1
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags =soup('a')
