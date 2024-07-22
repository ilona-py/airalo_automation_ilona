import allure
from source_shop import ApiLinks


@allure.title("Automate API Requests and Verify Responses")
def test_api_automation_chat(api_endpoints):
    with allure.step('Obtain OAuth2 tokens to access the Airalo Partner API'):
        api_endpoints.login()

    with allure.step('Create an order'):
        quantity = 6
        package_id = ApiLinks.merhaba_package
        submit_order_response = api_endpoints.post_submit_order(quantity=quantity,
                                                                package_id=package_id)
        create_order = submit_order_response.json()['data']

    with allure.step(f'Ensure the list contains {quantity} eSIMs, and {package_id} package slug'):
        assert 'sims' in create_order and len(create_order['sims']) == quantity, "Incorrect number of eSIMs in order."
        assert create_order['package_id'] == package_id, \
            f"Incorrect package_id. Expected: {package_id}, Found: {create_order['package_id']}"
        assert create_order['quantity'] == quantity, \
            f"Incorrect quantity. Expected: {quantity}, Found: {create_order['quantity']}"

    with allure.step("GET a list of eSIMs"):
        sims_response = api_endpoints.get_sims()
        sims = sims_response.json()['data'][0]

    with allure.step('Check the response body for correct information, including order details and eSIM properties'):
        assert sims['id'] == create_order['id']
        assert sims['code'] == create_order['code']
        assert sims['currency'] == create_order['currency'] == 'USD'
        assert sims['type'] == create_order['type'] == 'sim'
        assert sims['esim_type'] == create_order['esim_type'] == 'Prepaid'
        assert sims['validity'] == create_order['validity'] == 7
        assert sims['package'] in create_order['package']
        assert sims['data'] == create_order['data'] == '1 GB'
        assert sims['price'] == create_order['price'] == 4.5
        assert sims['created_at'] == create_order['created_at']
        assert (create_order['manual_installation'] in sims['manual_installation']
                and sims['manual_installation'] == ApiLinks.manual_installation)
        assert (create_order['qrcode_installation'] in sims['qrcode_installation']
                and sims['qrcode_installation'] == ApiLinks.qrcode_installation)
        assert sims['quantity'] == quantity
        assert sims['package_id'] == package_id
        assert sims['installation_guides']['en'] == create_order['installation_guides']['en'] == ApiLinks.guide

    with allure.step('Check each eSIM information'):
        sims_list = create_order['sims']
        for i in range(1, len(sims_list)):
            previous_sim = sims_list[i - 1]
            current_sim = sims_list[i]
        assert current_sim['id'] == previous_sim['id'] + 1, \
            f"Expected id {previous_sim['id'] + 1}, found {current_sim['id']}."
        assert current_sim['created_at'] == previous_sim['created_at']
        assert current_sim['lpa'] == previous_sim['lpa'] == 'lpa.airalo.com'
        assert current_sim['matching_id'] == previous_sim['matching_id'] == 'TEST'
        assert current_sim['apn_type'] == previous_sim['apn_type'] == 'manual'
        assert current_sim['apn_value'] == previous_sim['apn_value'] == 'airalo2'
        assert current_sim['is_roaming'] == previous_sim['is_roaming']
        assert current_sim['direct_apple_installation_url'] == previous_sim['direct_apple_installation_url']

    with allure.step('Check ICCID uniqueness and sequence'):
        iccids = [sim['iccid'] for sim in sims_list]
        for i in range(1, len(iccids)):
            previous_iccid = int(iccids[i - 1])
            current_iccid = int(iccids[i])
            assert current_iccid == previous_iccid + 1, \
                f"Expected iccid {previous_iccid + 1}, found {current_iccid}."
