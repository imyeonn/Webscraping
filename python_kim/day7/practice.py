# request
import urllib.request
req = urllib.request

# 웹서버 정보 파악
# getheaders() : 웹서버 정보를 리스트로 반환
d = req.urlopen("http://wikidocs.net/")
status = d.getheaders()
for s in status:
    print(s)
d.status
d.read()

# parse
import urllib.parse
def input_query()
    q = urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))
    return "&query=" +q

# os
import os
os.getcwd()
os.chdir("~/post")
os.listdir()
os.mkdir("~/post2")
os.makedirs("~/post2/ep1/sub1")
os.remove("~/post2/first.md")
os.unlink("~/post2/first.md")
os.rmdir("~/post2")
os.removedirs("~/post2")

# w
f = open("~/post/test.md", "w")
f.write("test writing")
f.close

# a
f = open("~/post/test.md", "a")
f.write("2test writing2")
f.close

with open("~/post/test.md", "a") as test:
    test.write("2test writing2")

# r
f = open("~/post/test.md", "r")
f.readline()
f.readlines()
lists = f.readlines()
    for list in lists:
        print(list)
f.close

# b
f = open("~/post/test.jpg", "rb")
f.read()
f.close
