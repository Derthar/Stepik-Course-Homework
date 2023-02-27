import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope='function')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser

    browser.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke  # Маркировка теста( все метки должны быть в файле pytest.ini)
    # @pytest.mark.skip  # Отмечает что данный тест нужно прпустить
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason='Fixing right now',strict=True)  # Отмечает тест как ожидаемо падающий
    # На выходе будет метка xfail. Если места xpass значит тес неождиданно прошел
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")
