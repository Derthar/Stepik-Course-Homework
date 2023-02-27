import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# @pytest.fixture(scope='function')
# def browser():
#     browser = webdriver.Chrome()
#     yield browser
#     browser.quit()

@pytest.mark.usefixtures
@pytest.mark.parametrize('num', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_stepik(browser, num):
    link = f'https://stepik.org/{num}/236895/step/1'
    browser.get(link)
    browser.delete_all_cookies()
    WebDriverWait(browser, 60, 0.5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#ember33')))
    browser.find_element(By.CSS_SELECTOR, '#ember33').click()
    browser.find_element(By.CSS_SELECTOR, 'input[name="login"]').send_keys('orilon229@mail.ru')
    browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('Galactica-75')
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn').click()
    time.sleep(10)
    WebDriverWait(browser, 30, 0.5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'textarea')))
    browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(str(math.log(int(time.time()))))
    WebDriverWait(browser, 30, 0.5).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    time.sleep(10)
    WebDriverWait(browser, 30, 0.5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints')))
    message = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    time.sleep(10)
    try:
        assert "Correct!" == message, 'Был введен неверный ответ на задачку'
    except AssertionError:
        with open('1.txt', 'a', encoding='utf-8') as file:
            file.write(message+'\n')
    time.sleep(5)
