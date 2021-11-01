from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from string import punctuation as punc
from collections import OrderedDict


def cleanInput(input):
    # 移除转义字符
    input = re.sub("\n+", " ", input)
    input = re.sub(" +", " ", input)
    # 转换为UTF-8字符集格式，以移除Unicode字符
    input = bytes(input, "UTF-8")
    input = input.decode('ascii', 'ignore')
    # 处理以得到分词结果
    cleanInput = []
    input = input.split(" ")
    for item in input:
        # 移除单词间的标点符号和引用标记
        item = item.strip(punc)
        # 移除除 'i' 'a' 外的单字符单词
        if len(item) > 1 or item.lower() not in ['i', 'a']:
            cleanInput.append(item)
    return cleanInput


def ngrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n + 1):
        output.append(input[i:i+n])
    return output


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, features="html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
# 去除重复的2-gram并按照指定的顺序排序，可以看到二元模型的数量从12303-->3386
ngrams = OrderedDict(ngrams, key=lambda t: t[1], reverse=True)
print(ngrams)
print("2-grams count is: " + str(len(ngrams)))
