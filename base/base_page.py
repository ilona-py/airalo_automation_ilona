from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """Base Page with common methods for work with web page"""

    url = None

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """Check if you currently at needed url
        :param url: full url to file
        """
        if self.driver.current_url == url:
            pass
        else:
            self.driver.get(self.url)
            self.wait_page_loaded()

    def wait_page_loaded(self):
        WebDriverWait(self.driver, 30).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete")
