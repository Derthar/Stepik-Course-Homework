from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'http://suninjuly.github.io/simple_form_find_task.html'
driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')
driver.get(url=url)

first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first_name']")
first_name.send_keys('Some First Name')

last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last_name']")
last_name.send_keys('Some Last Name')

city = driver.find_element(By.CSS_SELECTOR, "input[class='form-control city']")
city.send_keys('Some City')

country = driver.find_element(By.ID, "country")
country.send_keys('Some Country')

button = driver.find_element(By.CSS_SELECTOR, '#submit_button').click()

time.sleep(10)

driver.quit()
