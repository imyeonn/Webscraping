# 기본 세팅
import urllib.request
from bs4 import BeautifulSoup

# 내가 분석할 페이지 지정
TARGET1 = "http://section.blog.naver.com/sub/PostListByDirectory.nhn?option.page.currentPage="
TARGET2 = "&option.templateKind=0&option.directorySeq=18&option.viewType=default&option.orderBy=quality&option.latestOnly=1"
PAGES = 10

# 크롤링
for index in range(0, PAGES):
    with urllib.request.urlopen(TARGET1 + str(index + 1) + TARGET2)as url:
        data = url.read()
        bs = BeautifulSoup(data, "html.parser")

    query = bs.find_all('h5')
    for child in query:
        try:
            print(
                "%s\t" %
                (child.contents[0].string)
            )
        except AttributeError:
            pass
