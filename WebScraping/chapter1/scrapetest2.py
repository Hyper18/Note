from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
