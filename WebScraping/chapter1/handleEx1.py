from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    if html is None:
        print("This particular URL is not found.")
    bsObj = BeautifulSoup(html.read(), features="html.parser")
    print(bsObj.html.body.h1)
except HTTPError as e:
    print(e)
else:
    print("Keep Proceeding..")
