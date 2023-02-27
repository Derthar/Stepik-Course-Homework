from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 30, 0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))

browser.find_element(By.CSS_SELECTOR, 'button').click()

X =browser.find_element(By.CSS_SELECTOR, '#input_value').text
answer = str(math.log(abs(12*math.sin(int(X)))))
browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(answer)
browser.find_element(By.CSS_SELECTOR, '#solve').click()
time.sleep(10)

browser.quit()
