from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def setup(browser):
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(url=link)

def open_second_window():
    global driver
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    driver.switch_to.window(window_name=driver.window_handles[1])
    # Получаем список названий вкладок и переходим на вторую


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
    # time.sleep(2)
    open_second_window()
    # time.sleep(2)
    x = find_x(driver)
    # time.sleep(2)
    y = solve_the_equation(x)
    # time.sleep(2)
    fill_the_solvation(driver, y)
    # time.sleep(2)
    submit(driver)

    time.sleep(10)
    driver.quit()