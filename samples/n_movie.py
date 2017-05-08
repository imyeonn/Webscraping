import urllib.request

from bs4 import BeautifulSoup


def request_list(page):
    url = 'http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=127382&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}'
    url = url.format(page=page)

    res = urllib.request.urlopen(url)
    html = res.read()

    return BeautifulSoup(html, 'html.parser')


def fetch_comm_detail(soup):
    result = []
    
    li_tags = soup.find('div', class_='score_result').find_all('li')

    for li in li_tags:
        score_reple = li.find('div', class_='score_reple')
        content = score_reple.find('p')

        if content.span:
            content.span.extract()

        if content.span:
            content.span.extract()

        content = content.get_text(strip=True)                
        
        dt = score_reple.find('dl').find('dt')
        em_tags = dt.find_all('em')
        name = em_tags[0].find('span').get_text(strip=True)
        date = em_tags[1].get_text(strip=True)

        result.append({
            'content' : content,
            'name' : name,
            'date' : date
            })

    return result


for i in range(1, 4):
    soup = request_list(i)
    result = fetch_comm_detail(soup)
    print(result)

