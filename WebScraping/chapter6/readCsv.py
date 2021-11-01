from urllib.request import urlopen
from io import StringIO
import csv

# read html and ignore the rule of ascii coding
html = urlopen(
    "http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')

# use StringIO to perform encapsulation
file = StringIO(html)

# read lines
reader = csv.reader(file)
for row in reader:
    print("The album \""+row[0]+"\" was released in "+str(row[1]))
