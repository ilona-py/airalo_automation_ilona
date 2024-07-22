from selenium.webdriver.common.by import By


class HomePageLocators:
    search = (By.XPATH, "//input[@data-testid='search-input']")
    countries_list = (By.CLASS_NAME, 'countries-list position-absolute')
    japan_countries_list = (By.XPATH, "//ul//span[@data-testid='Japan-name']")
    users_advertising = (By.ID, 'ten-million-users-modal___BV_modal_body_')
    close_advertising = (By.XPATH, "//span[@data-testid='close-button']")
    accept_cookies = (By.ID, 'onetrust-accept-btn-handler')
    no_push_notifications = (By.ID, 'wzrk-cancel')


class JapanESimLocators:
    store_title = (By.ID, 'store-title')
    local_e_sims = (By.XPATH, "//ul//a[contains(text(), 'Local eSIMs')]")
    buy_now_first_el = (By.XPATH, "(//div[@class='sim-item-bottom']//button)[1]")
    sim_package_detail = (By.XPATH, "//div[@data-testid='package-detail']")
    sim_operator_title = (By.XPATH, "//div[@data-testid='sim-detail-operator-title']//p")
    coverage = (By.XPATH, "//div[@data-testid='package-detail']//p[@data-testid='COVERAGE-value']//..//p")
    data_gb = (By.XPATH, "//div[@class='sim-detail-top']//p[@data-testid='DATA-value']//..//p")
    validity = (By.XPATH, "//div[@class='sim-detail-top']//p[@data-testid='VALIDITY-value']//..//p")
    price = (By.XPATH, "//div[@class='sim-detail-top']//p[@data-testid='PRICE-value']//..//p")

