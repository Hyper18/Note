from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

import bs4

random.seed()


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


def getHistoryIPs(pageUrl):
    # edit the format for the historal page URL
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + \
        pageUrl+"&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, features="html.parser")
    # find the links with class attr "mw-userlink mw-anonuserlink"
    # use IP address to substitute the username
    ipAddresses = bsObj.findAll("a", {"class": "mw-userlink mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


links = getLinks("/wiki/Python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("---------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)
    newLink = links[random.randint(0, len(links)-1)].attr["href"]
    links = getLinks(newLink)
