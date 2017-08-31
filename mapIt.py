#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

# import webbrowser, sys, pyperclip
# if len(sys.argv) > 1:
#     # Get address from command line.
#     address = ' '.join(sys.argv[1:])
#
# else:
#     # Get address from clipboard.
#     address = pyperclip.paste()
#
# webbrowser.open('https://www.google.com/maps/place/' + address)

# import requests, bs4
# res = requests.get('http://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")
# type(noStarchSoup)
#
# exampleFile = open('https://www.google.co.kr/')
# exampleSoup = bs4.BeautifulSoup(exampleFile)
# type(exampleSoup)

import bs4
exampleFile = open('http://google.com')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#meta')
type(elems)
