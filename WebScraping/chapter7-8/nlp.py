from urllib.request import urlopen
from bs4 import BeautifulSoup
from re import sub
from string import punctuation as punc
import operator


def ngrams(input, n) -> dict:
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        temp = " ".join(input[i:i+n])
        if temp not in output:
            output[temp] = 0
        output[temp] += 1
    return output


def cleanInput(input) -> list:
    # 移除转义字符
    input = sub("\n+", " ", input)
    input = sub("\[0-9]\*", "", input)
    input = sub(" +", " ", input)
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
            if not isCommonWord(item):
                cleanInput.append(item)
    return cleanInput


def isCommonWord(word) -> bool:
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it", "i", "that", "for", "you", "he", "with", "on", "do", "say", "this", "they", "is", "an", "at", "but", "we", "his", "from", "that", "not", "by", "she", "or", "as", "what", "go", "their", "can", "who", "get", "if", "would", "her", "all", "my", "make", "about", "know", "will", "as", "up", "one", "time", "has",
                   "been", "there", "year", "so", "think", "when", "which", "them", "some", "me", "people", "take", "out", "into", "just", "see", "him", "your", "come", "could", "now", "than", "like", "other", "how", "then", "its", "our", "two", "more", "these", "want", "way", "look", "first", "also", "new", "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give", "many", "well"]
    return True if word.lower() in commonWords else False


content = str(
    urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
print(sortedNGrams)
print("2-grams count is: " + str(len(sortedNGrams)))
