import os
import sys
import urllib.request
from bs4 import BeautifulSoup
client_id = "8LZcwX63Pzq_gcNTLlFv"
client_secret = "hyovFoF5WY"

target = input('검색어를 입력하세요 : ')
encText = urllib.parse.quote(target)

url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
file = open('result.txt', 'w', encoding='utf-8')
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))

    xmlsoup = BeautifulSoup(response_body, 'html.parser')
    items = xmlsoup.find_all('item')

    for item in items:
        file.write('--------------------------\n')
        file.write('제목 : ' + item.title.get_text(strip=True) + '\n')
        file.write('주소 : ' + item.link.get_text(strip=True) + '\n')
        file.write('내용 : ' + item.description.get_text(strip=True) + '\n')
        file.write('\n')
    file.close()

else:
    print("Error Code:" + rescode)
