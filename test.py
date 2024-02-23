import os
import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from constants import *
from datetime import datetime


test_video = "https://www.cda.pl/video/1855306285/vfilm"


def get_link():
    driver = webdriver.Chrome()
    driver.get(test_video)

    elem = driver.find_element(By.XPATH, video_xpath)
    print(elem.get_attribute('class'))
    link = elem.find_element(By.TAG_NAME, 'video').get_attribute('src')
    print("video link: ",link)
    driver.close()
    return link


def download(link):
    random_name = random.randint(1,10000000)
    if not os.path.exists("downloaded files"):
        os.mkdir("downloaded files")

    file_name = "downloaded files\\"+ str(random_name) +".mp4"

    r = requests.get(link)
    if r.status_code != 200:
        print('error')
        return

    print('downloading...')

    with open(file_name, 'wb') as file:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)
    print('file downloaded')

def main():
    link = get_link()
    download(link)


main()
