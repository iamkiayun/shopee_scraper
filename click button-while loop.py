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
"""search"""
driver = webdriver.Chrome('C:\chromedriver/chromedriver.exe')

def search_url():
    url = 'https://shopee.com.my/search?keyword=basketball'
    driver.get(url)


search_url()

"""click"""
def click_english(wait_time=10):
    xpath_ = '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button'
    WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath_))).click()
    time.sleep(5)


click_english()


"""scroll to bottom"""
def __scroll_down_page(speed=8):
    current_scroll_position, new_height = 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")


"""put into list"""
def put_into_list(wait_time=10):
    href_list = []
    page_to_scrape = 2
    while len(href_list) < page_to_scrape*50:
        __scroll_down_page()
        xpath_ = '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[2]'
        raw = WebDriverWait(driver, wait_time).until(EC.element_to_be_clickable((By.XPATH, xpath_)))
        items = raw.find_elements_by_tag_name('a')
        for i in tqdm(items):
            href = i.get_attribute('href')
            href_dic = {'product link': href}
            href_list.append(href_dic)
        try:
            xpath_click_next_button4 = '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/button[11]'
            click_next2 = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath_click_next_button4))).click()
        except:
            try:
                xpath_click_next_button3 = '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/button[10]'
                click_next2 = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath_click_next_button3))).click()
            except:
                try:
                    xpath_click_next_button2 = '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/button[9]'
                    click_next2 = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath_click_next_button2))).click()
                except:
                    try:
                        xpath_click_next_button1 = '//*[@id="main"]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/button[8]'
                        click_next1 = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath_click_next_button1))).click()
                    except:
                            pass
    return(href_list)


"""convert to csv"""
import pandas as pd

def convert_to_csv():
    filename = 'href click button-while loop'
    pf = pd.DataFrame(put_into_list())
    pf.index +=1
    pf.to_csv(f'{filename}.csv')


convert_to_csv()