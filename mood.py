import os
import random
import sys
import math
import http.client
from lxml import html
import requests
import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup



'''import yahoofinance
import fortune
import fool
import forbes

'''
url = "http://fortune.com/2015/12/06/patriots-virtual-reality/?xid=yahoo_fortune"
html = urlopen(url)
beautifulhtml = BeautifulSoup(html.read(),"lxml")
content = beautifulhtml.find("div",  {"class":"article-body-text rail-offset"})
print(content)