import re
import sys
import html2text
from urllib.request import urlopen
from string import whitespace
from tracemalloc import stop
from turtle import end_fill
from bs4 import BeautifulSoup

url = "https://chudobadesign.com/LKPR_online_version.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

with open('version.txt', 'r') as file:
    currentVersion = (file.readlines())[0]

onlineVersion = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in onlineVersion.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
onlineVersion = '\n'.join(chunk for chunk in chunks if chunk)

print("Installed version is: ",currentVersion)
print("Online version is: ",onlineVersion)

if currentVersion == onlineVersion:
    print("Latest version installed :)")
    sys.exit()

f = open("version.txt", "w")
f.write(onlineVersion)
f.close()