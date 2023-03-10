from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixtures
def test_add_to_bucket_button(browser):
    item = browser.find_elements(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
    assert item is not None, 'Кнопка отсутствует на сайте'
    time.sleep(15)
