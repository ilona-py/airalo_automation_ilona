import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Base(object):
    """Base with common methods for work with web elements"""

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find_element()

    def find_element(self, time_wait=5):
        """
        Find the element and checks that an element is presented on the page during the given timeout limit
        :param time_wait: given timeout
        """
        try:
            element = WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located(locator=self.locator))
            self.web_element = element
        except TimeoutException:
            logging.error(f"Can't find the element by locator {self.locator}")
            return self

    def find_elements(self, time_wait=5):
        """
        Find the element and checks that an element is presented on the page during the given timeout limit
        :return: element obj
        """
        try:
            element = WebDriverWait(self.driver, time_wait).until(EC.presence_of_all_elements_located(self.locator))
            return element
        except TimeoutException:
            logging.error("Can't find the element by locator {}".format(self.locator))
            return self

    def click(self, time_wait=5):
        """
        Click on the element, wait till element is clickable
        :param time_wait: given timeout
        """
        element = WebDriverWait(self.driver, time_wait).until(EC.element_to_be_clickable(self.locator))
        element.click()
        return None

    def send_keys(self, text):
        """
        Click on the element, clear field, send text by parameter
        :param text: send text
        """
        self.click()
        self.web_element.clear()
        self.web_element.send_keys(text)
        return None

    @property
    def text(self, time_wait=5):
        """
        Get text out of web element
        :return: text
        """
        element = WebDriverWait(self.driver, time_wait).until(EC.visibility_of_element_located(locator=self.locator))
        text = element.text
        return text

    def visibility_of_element(self, time_wait=5):
        """
        Check visibility of located element with given timeout.
        :param time_wait: Time in seconds to wait for the element to become visible.
        :return: True if the element is visible within the timeout, False otherwise.
        """
        try:
            WebDriverWait(self.driver, time_wait).until(EC.visibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def get_any_property(self, property_name, time_wait=5):
        element = WebDriverWait(self.driver, time_wait).until(EC.presence_of_element_located(locator=self.locator))
        prop = element.get_attribute(property_name)
        return prop

    def wait_until_text_visible(self, text, time_wait=10):
        """
        Wait until text is present in the element.
        :param text: The text you want to wait for.
        :param time_wait: The timeout in seconds.
        :return: True if the text is visible within the timeout, False otherwise.
        """
        try:
            WebDriverWait(self.driver, time_wait).until(EC.text_to_be_present_in_element(self.locator, text))
            return True
        except TimeoutException:
            return False
