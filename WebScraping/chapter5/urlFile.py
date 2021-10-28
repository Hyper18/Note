from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, features="html.parser")
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve(imageLocation, "logo.jpg")
