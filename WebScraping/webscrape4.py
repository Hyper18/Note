from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen(
    "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
bsObj = BeautifulSoup(html, features="html.parser")
content = bsObj.get_text()

# pre coding
print(content)

content = bytes(content, 'UTF-8')
content = content.decode("UTF-8")

# after decoding
print(content)
