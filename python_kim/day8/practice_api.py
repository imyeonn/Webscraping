# 네이버 Open API를 이용하여 네이버 뉴스를 검색하는 크롤러 만들기
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

defaultURL = 'https://openaip.naver.com/v1/search/news.xml?'
sort = 'sort-sim'
start='&start=1'
display='&display=100'
query = '&query=' + urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))

fullURL = defaultURL + sort + start + display + query

print(fullURL)

file = open('~/Webscraping/python_kim/day8/practice_api.py', 'w', encoding = 'utf-8')

headers = {
    'Host' : 'openaip.naver.com',
    'User-Agent' : 'curl/7.43.0',
    'Accept' : '*/*',
    'Content-Type' : 'application/xml',
    'X-Naver-Client-Id' : 'KCH81eZXC7nO3aBoCGIW',
    'X-Naver-Client-Secret' : 'rVTw_guPkN'
}

req = urllib.request.Request(fullURL, headers=headers)
f = urllib.request.urlopen(req)

resultXML = f.read()
xmlsoup = BeautifulSoup(resultXML, 'html.parser')

items = xmlsoup.find_all('item')

for item in items:
    file.write('--------------------------\n')
    file.write('뉴스제목 : ' + item.title.get_text(strip=True) + '\n')
    file.write('요약내용 : ' + item.description.get_text(strip=True) + '\n')
    file.write('--------------------------\n')

file.close()
