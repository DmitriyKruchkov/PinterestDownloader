import os
import urllib
from requests import get
from bs4 import BeautifulSoup
from time import sleep
import datetime


def downloader(links):
    counter = 0
    name_of_dir = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    os.mkdir(name_of_dir)
    for link in links:
        counter += 1
        picture = BeautifulSoup(get(link).text, 'html.parser').find("img", 'hCL kVc L4E MIw').get("src")
        destination = f'./{name_of_dir}/{counter}.jpg'
        try:
            urllib.request.urlretrieve(picture, destination)
        except ConnectionError:
            continue
        sleep(1)
