import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def setup(browser):
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(url=link)
    #time.sleep(5)

def fill_first_name(browser, text):
    first_name = browser.find_element(By.CSS_SELECTOR, ".form-control[name='firstname']")
    first_name.send_keys(text)


def fill_last_name(browser, text):
    last_name = browser.find_element(By.CSS_SELECTOR, ".form-control[name='lastname']")
    last_name.send_keys(text)


def fill_email(browser, text):
    email = browser.find_element(By.CSS_SELECTOR, ".form-control[name='email']")
    email.send_keys(text)

def upload_file(browser, path):
    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(path)

def submit(browser):
    browser.find_element(By.CSS_SELECTOR, 'button').click()

if __name__ == '__main__':

    driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')

    setup(driver)
    fill_first_name(driver, 'Some name')
    fill_last_name(driver, 'Some last name')
    fill_email(driver, 'Some email')
    upload_file(driver, 'D:\\Repository\\Selenium\\stepik\\module 2\\file.txt')
    submit(driver)
    time.sleep(10)
    driver.quit()