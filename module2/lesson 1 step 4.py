from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def setup(browser):
    link = 'https://suninjuly.github.io/math.html'
    browser.get(url=link)
    time.sleep(5)


def find_x(browser):
    unknown = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    return unknown


def solve_the_equation(number):
    return str(math.log(abs(12*math.sin(int(number)))))


def fill_the_solvation(browser, answer):
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(answer)


def select_checkbox(browser):
    browser.find_element(By.CSS_SELECTOR, '.form-check-input[type = "checkbox"]').click()


def select_radiobutton(browser):
    browser.find_element(By.CSS_SELECTOR, 'label.form-check-label[for=robotsRule]').click()


def submit(browser):
    browser.find_element(By.CSS_SELECTOR, 'button').click()


if __name__ == '__main__':

    driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')

    setup(driver)

    x = find_x(driver)

    X = solve_the_equation(x)

    fill_the_solvation(driver, X)

    select_checkbox(driver)

    select_radiobutton(driver)

    submit(driver)

    time.sleep(5)

    driver.quit()
