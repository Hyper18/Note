from os import close
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# similar func to StringIO
wordFile = BytesIO(wordFile)
# use ZipFile to decompress, note: all docs file have already compressed to save space
document = ZipFile(wordFile)
# get content in the xml form
xml_content = document.read('word/document.xml')

word_obj = BeautifulSoup(xml_content.decode('utf-8'), features="lxml")
# get text strings by the order of <w:t> tags
textStrings = word_obj.findAll("w:t")
for textElem in textStrings:
    closeTag = ""
    try:
        style = textElem.parent.previousSbiling.find("w:pstyle")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        pass
    print(textElem.text)
    print(closeTag)
