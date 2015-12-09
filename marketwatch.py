from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "http://www.marketwatch.com/story/gold-steps-higher-taking-cues-from-softer-dollar-2015-12-09?siteid=yhoof2"
html = urlopen(url)
beautifulhtml = BeautifulSoup(html.read(),"lxml")
content = beautifulhtml.find("div",  {"id":"article-body"})
print(content)