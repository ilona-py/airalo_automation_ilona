from base import BasePage, Base
from source_shop.locators import HomePageLocators
from source_shop.data import HomePageLinks


class HomePage(BasePage):
    url = HomePageLinks.url

    @property
    def search(self):
        return Base(self.driver, HomePageLocators.search)

    @property
    def accept_cookies(self):
        return Base(self.driver, HomePageLocators.accept_cookies)

    @property
    def countries_list(self):
        return Base(self.driver, HomePageLocators.countries_list)

    @property
    def japan_countries_list(self):
        return Base(self.driver, HomePageLocators.japan_countries_list)

    @property
    def users_advertising(self):
        return Base(self.driver, HomePageLocators.users_advertising)

    @property
    def close_advertising(self):
        return Base(self.driver, HomePageLocators.close_advertising)

    @property
    def no_push_notifications(self):
        return Base(self.driver, HomePageLocators.no_push_notifications)

    def close_advertising_if_visible(self):
        """
        Check if the advertising element is visible and close it if it is.
        """
        try:
            if self.users_advertising.visibility_of_element():
                self.close_advertising.click()
        except Exception as e:
            print(f"An error occurred while trying to close the advertising: {e}")

    def click_no_push_notifications(self):
        """
        Check if the advertising element is visible and close it if it is.
        """
        try:
            if self.no_push_notifications.visibility_of_element():
                self.no_push_notifications.click()
        except Exception as e:
            print(f"An error occurred while trying to close the advertising: {e}")

    def search_for_country(self, country):
        self.search.send_keys(country)
        self.countries_list.visibility_of_element()
