## findAll로 리스트 추출

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html, "html.parser")

nameList = bs0bj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
