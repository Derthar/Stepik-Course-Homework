from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def setup(browser):
    link = 'http://suninjuly.github.io/selects1.html'
    browser.get(url=link)


def solve_the_equation(browser):
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    return num1+num2


def find_x(browser):
    unknown = int(browser.find_element(By.CSS_SELECTOR, 'img').get_attribute('valuex'))
    return unknown


def select(browser, answer):
    Select(browser.find_element(By.TAG_NAME, 'select')).select_by_visible_text(answer)


def submit(browser):
    browser.find_element(By.CSS_SELECTOR, 'button').click()


if __name__ == '__main__':

    driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')

    setup(driver)

    x = solve_the_equation(driver)

    select(driver, str(x))

    submit(driver)

    time.sleep(10)

    driver.quit()
