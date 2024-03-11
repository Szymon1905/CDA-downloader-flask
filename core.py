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
import requests
from bs4 import BeautifulSoup
from flask import send_file

video_name = ""
save_path = ""

def get_win_downloads_path():
    return 'downloaded\\'
    # return os.path.join(os.environ['USERPROFILE'], 'Downloads')


def get_video_data(video_link):
    global video_name
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_extension("extension/ublock_origin.crx")
    driver = webdriver.Chrome(options=options)

    driver.get(video_link)
    

    

    #video_name = driver.find_element(By.XPATH, video_name_xpath).text
    response = requests.get('https://www.cda.pl/video/38417557f/vfilm')
    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.select("h1")
    video_name = elements[0].text

    elem = driver.find_element(By.XPATH, video_xpath)
    link = elem.find_element(By.TAG_NAME, 'video').get_attribute('src')

    

    driver.close()
    return link


def download_video_from_link(link):
    global video_name, save_path

    # delete non non-alphanumeric characters from file name
    # video_name = re.sub(r'[^a-zA-Z0-9 ]', '', video_name)
    video_name = "video.mp4"
    print("Name - ", video_name)
    
    save_path = get_win_downloads_path() + video_name
    
    

    response = requests.get(link)

    if response.status_code != 200:
        print('network error')
        return

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)
    
    return save_path


    
    
    



