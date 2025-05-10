import pytest
from collections import namedtuple
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from data import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recowery_page import PasswordRecoweryPage

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--incognito')
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.fixture
def password_recowery_page(driver):
    password_recowery_page = PasswordRecoweryPage(driver)
    return password_recowery_page