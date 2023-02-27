from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def setup(browser):
    link = 'http://suninjuly.github.io/registration2.html'
    browser.get(url=link)
    time.sleep(5)


def fill_first_name(browser, text):
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
    first_name.send_keys(text)


def fill_last_name(browser, text):
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
    last_name.send_keys(text)


def fill_email(browser, text):
    email = browser.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
    email.send_keys(text)


def fill_phone(browser, text):
    phone = browser.find_element(By.CSS_SELECTOR, ".second_block input.form-control.first")
    phone.send_keys(text)


def fill_address(browser, text):
    adress = browser.find_element(By.CSS_SELECTOR, ".second_block input.form-control.second")
    adress.send_keys(text)


def positive_min_test(browser, message):
    setup(browser)
    fill_first_name(browser, 'Some first name')
    fill_last_name(browser, 'Some last name')
    fill_email(browser, 'Some email')
    fill_phone(browser, 'Some phone')
    fill_address(browser, 'Some adress')
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    assert message in browser.title, 'Minimal positive test failed'
    print('Minimal positive test passed')


def positive_max_test(browser, message):
    setup(browser)
    fill_first_name(browser, 'Some first name')
    fill_last_name(browser, 'Some last name')
    fill_email(browser, 'Some email')
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    assert message in browser.title, 'Maximum positive test failed'
    print('Maximum positive test passed')


def negarive_test(browser, message):
    setup(browser)
    fill_first_name(browser, 'Some first name')
    fill_last_name(browser, 'Some last name')
    browser.find_element(By.CSS_SELECTOR, 'button').click()
    assert message not in browser.title, 'Negative test failed'
    print('Negative test passed')


if __name__ == '__main__':
    # TODO Необходимо указать свой путь до хромдрайвера, иначе не запустится
    driver = webdriver.Chrome() # (executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')

    succes_title = 'Welcome'

    positive_min_test(driver, succes_title)

    positive_max_test(driver, succes_title)

    negarive_test(driver, succes_title)

    time.sleep(10)

    driver.quit()
