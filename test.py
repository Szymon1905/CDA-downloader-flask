import os
import random
import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants import *
from datetime import datetime
import os

test_video = "https://www.cda.pl/video/1855306285/vfilm"
video_name = ""


def get_win_downloads_path():
    return os.path.join(os.environ['USERPROFILE'], 'Downloads')


def get_video_data():
    global video_name
    options = webdriver.ChromeOptions()
    options.add_extension("extension/ublock_origin.crx")
    driver = webdriver.Chrome(options=options)

    driver.get(test_video)

    video_name = driver.find_element(By.XPATH, video_name_xpath).text
    print("video name: ", video_name)

    elem = driver.find_element(By.XPATH, video_xpath)
    link = elem.find_element(By.TAG_NAME, 'video').get_attribute('src')
    print("video link: ", link)

    driver.close()
    return link


def download(link):
    global video_name

    # delete non non-alphanumeric characters from file name
    video_name = re.sub(r'[^a-zA-Z0-9 ]', '', video_name)

    # create save path
    save_path = get_win_downloads_path() + "\\" + video_name + ".mp4"

    print("save path: ", save_path)

    response = requests.get(link)

    if response.status_code != 200:
        print('network error')
        return

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)
    print('file downloaded: ',video_name)


def main():
    link = get_video_data()
    download(link)


main()
