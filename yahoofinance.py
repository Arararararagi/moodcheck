from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://finance.yahoo.com/news/trump-takes-biggest-lead-yet-190000121.html"
html = urlopen(url)
beautifulhtml = BeautifulSoup(html.read(),"lxml")
content = beautifulhtml.find("div",  {"class":"body yom-art-content clearfix"}).findAll("p")
print(content)