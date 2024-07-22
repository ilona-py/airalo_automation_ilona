from base import BasePage, Base
from source_shop.locators import JapanESimLocators


class JapanESimPage(BasePage):

    @property
    def store_title(self):
        return Base(self.driver, JapanESimLocators.store_title)

    @property
    def local_e_sims(self):
        return Base(self.driver, JapanESimLocators.local_e_sims)

    @property
    def esim_buy_now_first_el(self):
        return Base(self.driver, JapanESimLocators.buy_now_first_el)

    @property
    def sim_package_detail(self):
        return Base(self.driver, JapanESimLocators.sim_package_detail)

    @property
    def sim_operator_title(self):
        return Base(self.driver, JapanESimLocators.sim_operator_title)

    @property
    def coverage(self):
        return Base(self.driver, JapanESimLocators.coverage)

    @property
    def data_gb(self):
        return Base(self.driver, JapanESimLocators.data_gb)

    @property
    def validity(self):
        return Base(self.driver, JapanESimLocators.validity)

    @property
    def price(self):
        return Base(self.driver, JapanESimLocators.price)

    def get_coverage(self):
        return [element.text for element in self.coverage.find_elements()]

    def get_data_gb(self):
        return [element.text for element in self.data_gb.find_elements()]

    def get_validity(self):
        return [element.text for element in self.validity.find_elements()]

    def get_price(self):
        return [element.text for element in self.price.find_elements()]
