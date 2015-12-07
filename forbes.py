from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://www.forbes.com/sites/adamhartung/2015/12/06/how-bad-leadership-doomed-yahoo-ceo-mistakes-are-costly/?utm_campaign=yahootix&partner=yahootix"
html = urlopen(url)
beautifulhtml = BeautifulSoup(html.read(),"lxml")
content = beautifulhtml.find("div",  {"class":"article-text"})
print(content)