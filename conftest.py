import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # параметр командной строки для выбора браузера
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # параметр командной строки для выбора языка
    parser.addoption('--language', action='store', default=None,    # парамерт
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    # объявляем переменную для браузера
    browser_name = request.config.getoption("browser_name")
    # объявляем переменную для языка
    entire_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # объявление языка для chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': entire_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # объявление языка для firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", entire_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

