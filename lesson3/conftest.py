import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('--language')
    browser = webdriver.Chrome()
    languages = ['ru', 'fr', 'es', 'en', 'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'fi', 'it', 'ko', 'nl',
                 'pl', 'pt', 'pt-br', 'ro', 'sk', 'zh-cn', 'uk']
    if language in languages:
        browser.get(f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/')
    else:
        raise pytest.UsageError(f"--language should be one of the following : {languages}")
    yield browser
    browser.quit()
