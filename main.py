# importing the BeautifulSoup Library
import os
import shutil
from os.path  import basename
from urllib.parse import urlparse

import bs4
import requests
from pathlib import Path
import subprocess


def download_image(image, i):
    response = requests.get(image, stream=True)
    #a = urlparse(image)

    #realname = os.path.basename(a.path)+str(i)
    p = Path(image)
    realname = p.stem+str(i)
    file = open("./img/{}.jpg".format(realname), 'wb')

    response.raw.decode_content = True
    shutil.copyfileobj(response.raw, file)
    del response


# Creating the requests

res = requests.get("https://szyby24.pl/pl/przednie-w901/17496-mercedes-sprinter-vw-lt-1995-2006-wysoki-92cm---2000010057375.html")
print("The object type:", type(res))

# Convert the request object to the Beautiful Soup Object
soup = bs4.BeautifulSoup(res.text, 'html5lib')
print("The object type:", type(soup))

imgs = soup.findAll("a", {"class": "fancybox"})
i=1
for img in imgs:
    imgUrl = img['href'] # get the href from the tag
    download_image(imgUrl,i)
    i=i+1
    # cmd = [ 'wget', imgUrl ] # just download it using wget.
    # subprocess.Popen(cmd) # run the command to download
    # # if you don't want to run it parallel;
    # # and wait for each image to download just add communicate
    # subprocess.Popen(cmd).communicate()

for link in soup.find_all("a"):
    lnk = str(link.get("href"))
    if lnk.find('jpg',0)>0:
        with open(basename(lnk), "wb") as f:
            f.write(requests.get(lnk).content)
        print("Inner Text is: {}".format(link.text))
        print("Title is: {}".format(link.get("title")))
        print("href is: {}".format(link.get("href")))

