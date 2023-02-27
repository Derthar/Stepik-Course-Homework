from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def setup(browser):
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(url=link)

def accept_asert(browser):
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    browser.switch_to.alert.accept()


def find_x(browser):
    unknown = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    return unknown


def solve_the_equation(number):
    return str(math.log(abs(12*math.sin(int(number)))))


def fill_the_solvation(browser, answer):
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(answer)


def submit(browser):
    browser.find_element(By.CSS_SELECTOR, 'button').click()


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')
    setup(driver)

    accept_asert(driver)

    x = find_x(driver)

    y = solve_the_equation(x)

    fill_the_solvation(driver, y)

    submit(driver)

    time.sleep(10)
    driver.quit()