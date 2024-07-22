import allure
from source_shop import JapanESimLinks


@allure.title("Verify package details Japan")
def test_ui_automation(open_home_page, home_page, japan_esim):
    with allure.step("Close advertising if visible"):
        home_page.close_advertising_if_visible()
    with allure.step("Search for Japan"):
        home_page.accept_cookies.click()
        home_page.click_no_push_notifications()
        home_page.search_for_country(JapanESimLinks.japan)
        home_page.japan_countries_list.click()
        japan_esim.store_title.wait_until_text_visible(JapanESimLinks.japan)
        assert JapanESimLinks.active_tab in japan_esim.local_e_sims.get_any_property('class')
    with allure.step("Select an eSIM Package:"):
        japan_esim.esim_buy_now_first_el.click()
        japan_esim.sim_package_detail.visibility_of_element()
    with allure.step("Verify Package Details:"):
        assert japan_esim.sim_operator_title.text == JapanESimLinks.moshi
        assert japan_esim.get_coverage() == JapanESimLinks.coverage_japan
        assert japan_esim.get_data_gb() == JapanESimLinks.data_gb
        assert japan_esim.get_validity() == JapanESimLinks.validity
        assert japan_esim.get_price() == JapanESimLinks.price
