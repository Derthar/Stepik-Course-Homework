from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = 'http://suninjuly.github.io/find_link_text'
driver = webdriver.Chrome(executable_path='D:\\Repository\\Selenium\\SDET\\chromedriver\\chromedriver.exe')
driver.get(url=url)

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
driver.find_element(By.LINK_TEXT, link_text).click()

first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first_name']")
first_name.send_keys('Some First Name')

last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last_name']")
last_name.send_keys('Some Last Name')

city = driver.find_element(By.CSS_SELECTOR, "input[class='form-control city']")
city.send_keys('Some City')

country = driver.find_element(By.ID, "country")
country.send_keys('Some Country')

button = driver.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(10)

driver.quit()
