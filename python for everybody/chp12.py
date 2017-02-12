import urllib
from BeautifulSoup import *

url = raw_input('Enter : ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# 모든 a 태그 가져오기
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
