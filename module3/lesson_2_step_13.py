from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class TestSite(unittest.TestCase):
    def test_1(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.link = 'http://suninjuly.github.io/registration1.html'
        self.driver.get(url=self.link)

        first_name = self.driver.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
        first_name.send_keys('Some first name')

        last_name = self.driver.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
        last_name.send_keys('Some last name')

        email = self.driver.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
        email.send_keys('Some email')

        phone = self.driver.find_element(By.CSS_SELECTOR, ".second_block input.form-control.first")
        phone.send_keys('Some phone')

        adress = self.driver.find_element(By.CSS_SELECTOR, ".second_block input.form-control.second")
        adress.send_keys('Some adress')
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()
        self.assertIn('Welcome', self.driver.title, 'Minimal positive test failed')
        # assert message in self.driver.title, 'Minimal positive test failed'
        print('Minimal positive test passed')
        self.driver.quit()

    def test_2(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.link = 'http://suninjuly.github.io/registration2.html'
        self.driver.get(url=self.link)

        first_name = self.driver.find_element(By.CSS_SELECTOR, ".first_block input.form-control.first")
        first_name.send_keys('Some first name')

        last_name = self.driver.find_element(By.CSS_SELECTOR, ".first_block input.form-control.second")
        last_name.send_keys('Some last name')

        email = self.driver.find_element(By.CSS_SELECTOR, ".first_block input.form-control.third")
        email.send_keys('Some email')

        phone = self.driver.find_element(By.CSS_SELECTOR, ".second_block input.form-control.first")
        phone.send_keys('Some phone')

        adress = self.driver.find_element(By.CSS_SELECTOR, ".second_block input.form-control.second")
        adress.send_keys('Some adress')
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()
        self.assertIn('Welcome', self.driver.title, 'Negative test failed')
        # assert message not in self.driver.title, 'Negative test failed'
        print('Negative test passed')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
