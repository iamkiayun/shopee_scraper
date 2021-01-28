"""import library"""
from tqdm import tqdm
import time, urllib.request, requests, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

"""start coding"""

driver = webdriver.Chrome('C:\chromedriver/chromedriver.exe')
url = 'https://shopee.com.my/search?keyword=basketball'
driver.get(url)

click_on_english = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button'))).click()
time.sleep(5)

# scroll to bottom
"""
pause_time = 5
# get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:

    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # calculate new scroll height and compare with the last scroll height

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break

    last_height = new_height

"""
"""
def __scroll_down_page(self, speed=8):
    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        self.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = self.execute_script("return document.body.scrollHeight")
"""

current_scroll_position, new_height= 0, 1
speed = 8
while current_scroll_position <= new_height:
    current_scroll_position += speed
    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
    new_height = driver.execute_script("return document.body.scrollHeight")

href_list = []
raw = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[2]')))
items = raw.find_elements_by_tag_name('a')
for i in tqdm(items):
    href = i.get_attribute('href')
    href_list.append(href)

import pandas as pd
pf = pd.DataFrame(href_list)

pf.to_csv('href_test2.csv')





