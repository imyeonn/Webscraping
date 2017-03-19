import requests
from lxml import html

response = requests.get('http://www.coupang.com/')
assert response.status_code == 200
tree = html.fromstring(response.content)

print("****쿠팡 카테고리****")
file = open('result.txt', 'w', encoding='utf-8')
file.write("****쿠팡 카테고리****\n")
for i in tree.xpath("//select[@class='search_category_filter']/option"):
    if i.text == '전체':
        continue
    else:
        print(i.text)
        try:
            response2 = requests.get(
                'http://www.coupang.com/' + i.get('value'))
            assert response2.status_code == 200
            tree2 = html.fromstring(response2.content)
            for j in tree2.xpath("//ul[@class='nav-items']/li/a"):
                print("         " + j.text.strip())
                file.write("         " + j.text.strip() + '\n')

                try:
                    response3 = requests.get(
                        'http://www.coupang.com/' + j.get('href'))
                    assert response3.status_code == 200
                    tree3 = html.fromstring(response3.content)
                    for k in tree3.xpath("//li[@class='nav-item']/a"):
                        print("                      " + k.text.strip())
                        file.write("                      " + k.text.strip() + '\n')
                except:
                    pass

        except:
            pass

file.close()
