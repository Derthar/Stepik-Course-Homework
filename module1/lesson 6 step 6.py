from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

url = 'http://suninjuly.github.io/huge_form.html'
driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')
driver.get(url=url)

input_elements = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")

for elem in input_elements:
    elem.send_keys('Some Text')

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(10)

driver.quit()
