from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://www.fool.com/investing/general/2015/12/06/alphabet-incs-new-google-glass-is-bound-to-be-anot.aspx"
html = urlopen(url)
beautifulhtml = BeautifulSoup(html.read(),"lxml")
content = beautifulhtml.find("div",  {"class":"main-col"}).find("section", {"class":"usmf-new article-body"}).find("span", {"class":"article-content"})
print(content)