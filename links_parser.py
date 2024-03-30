from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from config import TIME_FOR_REQUEST


def links_parser(nums, word):

    word = "%20".join(word.split())
    url = f"https://www.pinterest.com/search/pins/?q={word}&rs=typed"

    not_processed_links = set()
    with (webdriver.Firefox() as browser):
        browser.get(url)
        sleep(TIME_FOR_REQUEST)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        not_processed_links.update(set(soup.find('div', "vbI XiG").find_all('a')))
        last_height = browser.execute_script("return document.body.scrollHeight")
        while len(not_processed_links) // 2 < nums:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(TIME_FOR_REQUEST)
            soup = BeautifulSoup(browser.page_source, "html.parser")
            not_processed_links.update(set(soup.find('div', "vbI XiG").find_all('a')))
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    links = set()
    for elem in not_processed_links:
        links.add(f"https://www.pinterest.com{elem.get("href")}")

    return list(links)[:nums]
