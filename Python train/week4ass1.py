import urllib2

from bs4 import BeautifulSoup

url = "http://python-data.dr-chuck.net/comments_314694.html"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)

sum = 0
tags = soup('span10')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('span', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
    
    sum = sum + int(tag.contents[0])
    print sum