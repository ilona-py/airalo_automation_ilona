import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages import HomePage, JapanESimPage
from api import ApiEndpoints


@pytest.fixture(scope='session')
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def home_page(get_driver):
    return HomePage(get_driver)


@pytest.fixture(scope="session")
def japan_esim(get_driver):
    return JapanESimPage(get_driver)


@pytest.fixture(scope="function")
def open_home_page(home_page):
    home_page.open_url(url=home_page.url)
    yield


@pytest.fixture(scope="session")
def api_endpoints():
    return ApiEndpoints()
