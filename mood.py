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
from urllib.parse import urlparse
import re
import http.cookiejar
import time

cj = http.cookiejar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]


def main():
    try:
        page = 'http://feeds.finance.yahoo.com/rss/2.0/headline?s=GOOG&region=US&lang=en-US'
        sourceCode = opener.open(page).read()
        #print sourceCode

        try:
            titles = re.findall(r'',sourceCode)
            links = re.findall(r'(.*?)',sourceCode)
            for title in titles:
                print (title)
            for link in links:
                print (link)
        except Exception as e:
            print (str(e))

    except Exception as e:
        print (str(e))
        pass

main()

parsed_uri = urlparse(url)
domain = "{uri.netloc}".format(uri=parsed_uri)
print(domain)