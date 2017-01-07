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
