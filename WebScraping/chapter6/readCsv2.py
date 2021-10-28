from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import StringIO
import csv

# read html and ignore the rule of ascii coding
html = urlopen(
    "http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')

# use StringIO to perform encapsulation
file = StringIO(html)

# read lines
reader = csv.DictReader(file)
# print(reader.fieldnames) 省去的首行类型信息
for row in reader:
    print(row)
