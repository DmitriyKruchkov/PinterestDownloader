import asyncio
import datetime
import os

import aiohttp
from bs4 import BeautifulSoup
from requests import get


async def downloader(links):
    counter = 0
    name_of_dir = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    print(f"Имя папки для загрузки: {name_of_dir}")
    tasks = []
    session = aiohttp.ClientSession()
    for link in links:
        counter += 1
        picture_url = BeautifulSoup(get(link).text, 'html.parser').find("img", 'hCL kVc L4E MIw').get("src")
        if not os.path.exists("./output"):
            os.mkdir("./output")
        if not os.path.exists(f'./output/{name_of_dir}'):
            os.mkdir(f'./output/{name_of_dir}')
        destination = f'./output/{name_of_dir}/{counter}.jpg'
        task = asyncio.create_task(get_file(picture_url, destination, session))
        tasks.append(task)
    await asyncio.gather(*tasks)
    await session.close()


async def get_file(url, destination, session):
    try:
        response = await session.get(url)
        await write_file(destination, response)
    except ConnectionError:
        pass


async def write_file(destination, response):
    data = await response.read()
    with open(destination, 'wb') as file:
        file.write(data)
