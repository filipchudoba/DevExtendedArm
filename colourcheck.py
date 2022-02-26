import re
import sys
import html2text
from urllib.request import urlopen
from string import whitespace
from tracemalloc import stop
from turtle import end_fill
from bs4 import BeautifulSoup


url = "https://chudobadesign.com/LKPR_lights.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

textik = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in textik.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
textik = '\n'.join(chunk for chunk in chunks if chunk)

res = tuple(map(str, textik.split(',')))

colourList = res
