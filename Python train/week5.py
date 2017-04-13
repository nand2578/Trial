
import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_314691.xml'

data = urllib.urlopen(url).read()
tree = ET.fromstring(data)

#Using an XPath selector string to look through the entire tree of XML for any tag named 'count'
counts = tree.findall('.//count')

total_sum = 0
for i in counts:
    total_sum = total_sum + int(i.text)
print total_sum