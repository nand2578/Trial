import urllib
import re
position = raw_input('Enter Position')
count = raw_input('Enter count')

url = 'http://python-data.dr-chuck.net/known_by_Tamta.html'
html = urllib.urlopen(url).read()
link = re.findall('href="(http://.*?)"', html)[int(position)-1]
print link

i = 1
while i < int(count):
    i = i+1
    url = str(link)
    html = urllib.urlopen(url).read()
    link = re.findall('href="(http://.*?)"', html)[2]
    print link