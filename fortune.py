from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://fortune.com/2015/12/06/patriots-virtual-reality/?xid=yahoo_fortune"
html = urlopen(url)
beautifulhtml = BeautifulSoup(html.read(),"lxml")
content = beautifulhtml.find("div",  {"class":"article-body-text rail-offset"})
print(content)