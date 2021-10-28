from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
# similar func to StringIO
wordFile = BytesIO(wordFile)
# use ZipFile to decompress, note: all docs file have already compressed to save space
document = ZipFile(wordFile)
# get content in the xml form
xml_content = document.read('word/document.xml')
print(xml_content.decode('utf-8'))
