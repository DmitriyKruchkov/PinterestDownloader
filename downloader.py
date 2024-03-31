import datetime
import os
import urllib
from time import sleep

from bs4 import BeautifulSoup
from requests import get


def downloader(links):
    counter = 0
    name_of_dir = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    os.mkdir(name_of_dir)
    for link in links:
        counter += 1
        picture = BeautifulSoup(get(link).text, 'html.parser').find("img", 'hCL kVc L4E MIw').get("src")
        if not os.path.exists("./output"):
            os.mkdir("./output")
        destination = f'./output/{name_of_dir}/{counter}.jpg'
        try:
            urllib.request.urlretrieve(picture, destination)
        except ConnectionError:
            continue
        sleep(1)
