from bs4 import BeautifulSoup
bs=BeautifulSoup(html, "html.parser")

# find
bs.find("title")
bs.find("p", align="left")
bs.find("p", class_="text")

# find_all
bs.find_all("p")
bs.find_all("p", limit=2)
bs.find_all(text="text contents 1")
bs.find_all(text=re.compile("text +"))

# string, strings
body_tag = bs.find("body")
p_tag = body_tag.find_all("p")

string = body_tag.find("p")

strings = p_tag.strings
for strings_comp in strings :
    print(string_comp)

# get_text
body_tag.get_text()
body_tag.get_text(strip=True)
body_tag.get_text(',', strip=True)

# find_parent, find_parents
p_tag.find_parent("body")
parents = p_tab.find_parents()
for parent in parents:
    print (parent.name)


### 0905 전체 쇼핑몰 리스트 순위 및 조회수 출력 &매주 변화추이 파악 ###

# 웹사이트에 접근할 수 있는 도구상자 urllib request, bs 가져오기
import urllib.request
from bs4 import BeautifulSoup

# sort=F 뒤 &page=1, 2, 3... for문으로 1-28페이지 접근
TARGET = "http://www.style-chart.com/rank/?&sort=F&page="
PAGES = 28

# 각 페이지별로 정보 읽어서 뷰티풀수프 실행
for index in range(0, PAGES):
    with urllib.request.urlopen(TARGET + str(index + 1))as url:
        data = url.read()
        soup = BeautifulSoup(data, "html.parser")

    # 실행시킨 bs에 아까 크롬 검사에서 확인한 info2 클래스를 전체화면에서 검색
    query = soup.find_all('li', attrs={'class': 'info2'})

    # 그렇게 찾은 데이터를 for로 화면출력
    for child in query:
        try:
            print(
                "%s\t%s" %
                (child.contents[1].strong.string, child.contents[-4].contents[-1].string)
            )


        except AttributeError:
            pass

            # child.contents[1].strong은 위 child 리스트의 2번째 줄이 쇼핑몰이름이고 양쪽에 strong 태그로 둘러싸임
            # 여기서 <strong>쇼핑몰이름</strong> 태그 제외할거면 .string
