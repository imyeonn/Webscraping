import urllib.request
import urllib.parse
import time

from bs4 import BeautifulSoup


def fetch_post_list(keyword, page):
    url = 'http://section.blog.naver.com/sub/SearchBlog.nhn?type=post&option.keyword={keyword}&term=&option.startDate=&option.endDate=&option.page.currentPage={page}&option.orderBy=sim'    
    url = url.format(keyword=keyword, page=page)
    
    res = urllib.request.urlopen(url)
    html = res.read()

    soup = BeautifulSoup(html, 'html.parser')


    li_tags = soup.find_all('li', class_='add_img')

    result = []
    for li in li_tags:
        a_tag = li.find('h5').find('a')
        title = a_tag.get_text(strip=True)
        href = a_tag['href']
        result.append({
            'title': title,
            'href': href
            })

    return result



def fetch_blog_data(soup):
    
    result = {
        'date' : '',
        'content' : '',
        'title' : soup.find('h3', class_='se_textarea')
        }
    
    if result['title']:
        result['title'] = result['title'].get_text(strip=True)
        result['date'] = soup.find('span', class_='se_publishDate').get_text(strip=True)
        result['content'] = soup.find('div', class_='sect_dsc').get_text(strip=True)
    else:
        result['title'] = soup.find('span', class_='pcol1').get_text(strip=True)
        result['date']  = soup.find('p', class_='_postAddDate').get_text(strip=True)
        result['content'] = soup.find('div', id='postViewArea').get_text(strip=True)

    return result

def fetch_blog(url):

    res = urllib.request.urlopen(url)
    html = res.read()

    soup = BeautifulSoup(html, 'html.parser')

    result = fetch_blog_data(soup)
    return result

def find_mainFrame(url):
    mainFrame_src = ''
    
    def request(url):
        print(url)
        res = urllib.request.urlopen(url)
        html = res.read()

        return BeautifulSoup(html, 'html.parser')

    while True:
        soup = request(url)
        if soup.find('frame', id='screenFrame'):
            url = soup.find('frame', id='screenFrame')['src']
            time.sleep(5)
            continue
        else:
            mainFrame_src = 'http://blog.naver.com' + soup.find('frame', id='mainFrame')['src']
            break

    return mainFrame_src


f = open('test.txt', 'w', encoding='utf-8')

keyword = input('검색어를 입력하세요: ')
keyword = urllib.parse.quote(keyword)

result = fetch_post_list(keyword, 1)

count = 0

for r in result:
    mainFrame_src = find_mainFrame(r['href'])
    
    data = fetch_blog(mainFrame_src)

    f.write('==' * 40 + '\n')
    f.write('타이틀: ' + data['title'] + '\n')
    f.write('날짜: ' + data['date'] + '\n')
    f.write('내용: ' + data['content'] + '\n')
    f.write('==' * 40 + '\n')
    time.sleep(5)
    count += 1
    if count == 5:
        break

f.close()




































