
#필요한 모듈들 import
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

import re

import time

#url = 'http://sotong.yongin.go.kr/front/boardList.do?brd_mgrno=1&&page_now={page}'

def request_url(page):
    url = 'http://sotong.yongin.go.kr/front/boardList.do?brd_mgrno=1&&page_now={page}'
    url = url.format(page=page)
    res = urllib.request.urlopen(url)
    html = res.read()

    return html

def fetch_post_list(soup):
    result = []
    a_tags = soup.find_all('a', class_='eliptxt3')
    
    for a in a_tags:
        
        title = a['title']
        href = re.search('[0-9]+', a['href']).group()

        result.append({
            'title' : title,
            'href' : href
            })

    return result


def fetch_post_detail(page, brd_no):
    url = 'http://sotong.yongin.go.kr/front/boardView.do'

    param = {
        'mwkeykind':'all',
        'keyword':'',
        'etc_field1':'',
        'etc_field3':'',
        'page_now':'{page}'.format(page=page),
        'returl':'/front/boardList.do?brd_mgrno=1',
        'brd_mgrno':'1',
        'brd_no':'{brd_no}'.format(brd_no=brd_no),
        'menu_no':'',
        'param':'brd_mgrno=1&page_now={page}'.format(page=page),
        'tp':''
    }

    param = urllib.parse.urlencode(param).encode()

    req = urllib.request.Request(url, param)
    res = urllib.request.urlopen(req)

    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')

    tr_tags = soup.find('div', class_='table').find_all('tr')

    return tr_tags[4].get_text(strip=True)


for i in range(1, 4):
    html = request_url(i)
    soup = BeautifulSoup(html, 'html.parser')
    result = fetch_post_list(soup)
    
    for r in result:
        time.sleep(5)
        q = fetch_post_detail(i, r['href'])
        
        break
    
