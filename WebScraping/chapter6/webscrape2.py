from urllib.request import urlopen
textPage2 = urlopen(
    "http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")

print(textPage2.read(), 'utf-8')
