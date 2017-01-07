import os
import time

import urllib.parse
import random

import re

from bs4 import BeautifulSoup
from datetime import datetime

def input_query(quote="plus"):
    query = input("검색할 문자열을 입력하세요: ")

    if quote == "plus":
        query = urllib.parse.quote_plus(query)
    elif quote == "space":
        query = urllib.parse.quote(query)

    return query

def input_count():
    count = int(input("검색할 게시물의 개수를 입력하세요('10단위'): "))

    return count

def input_delay():
    delay = int(input("요청의 간격을 초 단위로 입력하세요: "))

    return delay

    def input_save_path():
    path = str(input("저장 경로를 입력하세요: "))
    path = path.replace("\\", "/")

    if not os.path.isdir(os.path.split(path)[0]):
        os.mkdir(os.path.split(path)[0])

    return path

def read_to_soup(url, headers):
    request = urllib.request.Request(url, headers=headers)
    result = urllib.request.urlopen(request)
    html = result.read()
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def separation(file):
    file.write("==" * 30 + "\n")

def file_write(file, text):
    file.write(text + "\n")

def save_file(path):
    return open(path, 'w', encoding='utf-8')

def delay_random():
    val = random.randint(5, 10)
    time.sleep(val)
    print("%s초 기다렸습니다." % val)

def input_url():
    url = input("크롤링할 URL을 입력해주세요: ")
    return url

def input_catname():
    cat_name = input("검색할 게시판의 이름을 입력하세요: ")
    return cat_name

def input_cookie():
    cookie = input("쿠키값을 입력하세요:")
    return cookie

def func_loop(cb):
    while True:
        cb()

        ques = input("계속 검색 하시겠습니까?(Y, N): ")

        if ques == "Y":
            continue
        else:
            break

            def ask_mix_content():
    mix = int(input("1 : 질문만 출력하기 \n2 : 질문 + 답변 함께 출력하기 \n 원하는 작업 번호를 입력하세요: "))
    return mix


def N_detail_option():
    detailed_search = int(input("상세 검색 옵션을 사용하시겠습니까?(사용 : 1, 사용 안함 : 0)"))

    exactly_stc = ""
    certainly_word = ""
    except_word = ""

    if detailed_search:
        query = ""

        exactly_stc = str(input("정확히 일치하는 단어나 문장을 입력하세요: "))
        certainly_word = str(input("반드시 포함하는 단어를 입력하세요: "))
        except_word = str(input("제외할 단어를 입력하세요: : "))

        query += " "
        for stc in exactly_stc.split(","):
            query += "\"" + stc.strip() + "\""

        for word in certainly_word.split(","):
            query += " +" + word.strip()

        for word in except_word.split(","):
            query += " -" + word.strip()

        return urllib.parse.quote_plus(query)

    return ""

def N_search_date():
    date_setting = int(input("기간을 설정 하시겠습니까?(설정:1, 설정안함:0)"))

    if date_setting:
        t_pd = int(input("""
                1 = 1주
                2 = 1개월
                3 = 기간 입력
                입력: """))

        if t_pd == 1:
            return "&period=1w"

        elif t_pd == 2:
            return "&period=1m"

        elif t_pd == 3:

            if len(str(datetime.today().month)) == 1:
                dates = [datetime.today().year, '0' + str(datetime.today().month), datetime.today().day]
            else:
                dates = [datetime.today().year, str(datetime.today().month), datetime.today().day]

            while True:
                day_start = str(input("시작 날짜를 입력해 주세요(예: 2014-01-01): "))

                t_ds = re.match("^[0-9]{4}-[0-9][0-9]-[0-9][0-9]", day_start)
                t_ds_split = t_ds.string.split("-")

                if int(t_ds_split[1]) > 12:
                    print("12월 이상은 존재하지 않습니다.")
                    continue

                if int(t_ds_split[2]) > 31:
                    print("31일 이상은 존재하지 않습니다.")
                    continue

                if t_ds:

                    c = ""
                    d = ""

                    for i in range(0, 3):
                        c += str(dates[i])
                        d += str(t_ds_split[i])

                    if int(d) > int(c):
                        print("시작 날짜가 현재 날짜 보다 클수는 없습니다.")
                        continue

                    #df += day_start
                    break

                else:
                    print("잘못된 입력입니다.")
                    continue

            while True:
                day_end = str(input("종료 날짜를 입력해 주세요(예: 2014-01-01): "))

                t_de = re.match("^[0-9]{4}-[0-9][0-9]-[0-9][0-9]", day_end)
                t_de_split = t_de.string.split("-")

                if int(t_de_split[1]) > 12:
                    print("12월 이상은 존재하지 않습니다.")
                    continue

                if int(t_de_split[2]) > 31:
                    print("31일 이상은 존재하지 않습니다.")
                    continue

                if t_de:

                    t_ds_split = day_start.split("-")

                    c = ""
                    d = ""
                    s = ""

                    for i in range(0, 3):
                        c += str(dates[i])
                        d += str(t_de_split[i])
                        s += str(t_ds_split[i])

                    if int(d) > int(c):
                        print("종료 날짜가 현재 날짜 보다 클수는 없습니다.22")
                        continue

                    if int(s) > int(d):
                        print("시작 날짜가 종료 날짜 보다 클수는 없습니다.")
                        continue

                    #dt += day_end
                    break

                else:
                    print("잘못된 입력입니다.")
                    continue
            day_start = day_start.replace("-", ".") + "."
            day_end = day_end.replace("-", ".") + "."

            return "&period=" + urllib.parse.quote(day_start + "|" + day_end)

    return ""


def get_params_from_url(url):
    result = urllib.parse.urlparse(url)
    query = result[4]

    params = urllib.parse.parse_qsl(query)

    return params
