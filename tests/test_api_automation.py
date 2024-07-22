import allure
from source_shop import ApiLinks


@allure.title("Automate API Requests and Verify Responses")
def test_api_automation(api_endpoints):
    with allure.step('Obtain OAuth2 tokens to access the Airalo Partner API'):
        api_endpoints.login()

    with allure.step('Create an order'):
        quantity = 6
        package_id = ApiLinks.merhaba_package
        submit_order_response = api_endpoints.post_submit_order(quantity=quantity,
                                                                package_id=package_id)
        create_order = submit_order_response.json()['data']
        created_sims = create_order['sims']

    with allure.step(f'Ensure the list contains {quantity} eSIMs, and {package_id} package slug'):
        assert 'sims' in create_order and len(create_order['sims']) == quantity, "Incorrect number of eSIMs in order."
        assert create_order['package_id'] == package_id, \
            f"Incorrect package_id. Expected: {package_id}, Found: {create_order['package_id']}"
        assert create_order['quantity'] == quantity, \
            f"Incorrect quantity. Expected: {quantity}, Found: {create_order['quantity']}"

    with allure.step("GET a list of eSIMs"):
        sims_get = api_endpoints.get_sims()
        response_sims = sims_get.json()['data']

    with allure.step('Check the response body for correct information, including order details and eSIM properties'):
        assert len(response_sims) == 6, f"Expected 6 eSIMs, but found {len(response_sims)}"
        for sim in response_sims:
            assert sim['simable']['package_id'] == package_id, \
                f"Incorrect package_id in eSIM. Expected: {package_id}, Found: {sim['simable']['package_id']}"
        for created_sim in created_sims:
            created_id = created_sim['id']
            created_iccid = created_sim['iccid']

    with allure.step(f'Check SIM with ID {created_id}'):
        matching_sim = next((sim for sim in response_sims if sim['id'] == created_id), None)
        assert matching_sim is not None, f"ID {created_id} from created SIMs not found in response SIMs"

    with allure.step('Check if the iccid matches'):
        response_iccid = matching_sim['iccid']
        assert created_iccid == response_iccid, f"ICCID mismatch for ID {created_id}"

    with allure.step(f'Check if the package_id matches {ApiLinks.merhaba_package}'):
        response_package_id = matching_sim.get('simable', {}).get('package_id')
        assert response_package_id == ApiLinks.merhaba_package, f"Package ID mismatch for ID {created_id}"

    with allure.step(f'Check if the package_id matches {ApiLinks.expected_package}'):
        response_package = matching_sim.get('simable', {}).get('package')
        assert response_package == ApiLinks.expected_package, f"Package mismatch for ID {created_id}"

    with allure.step('Check other eSIM properties'):
        assert matching_sim.get('simable', {}).get('currency') == 'USD', f"Currency mismatch for ID {created_id}"
        assert matching_sim.get('simable', {}).get('quantity') == 6, f"Quantity mismatch for ID {created_id}"
        assert matching_sim.get('simable', {}).get('type') == 'sim', f"Type mismatch for ID {created_id}"
        assert matching_sim.get('simable', {}).get('esim_type') == 'Prepaid', f"eSIM type mismatch for ID {created_id}"
        assert matching_sim.get('simable', {}).get('validity') == '7', f"Validity mismatch for ID {created_id}"
        assert matching_sim.get('simable', {}).get('data') == '1 GB', f"Data mismatch for ID {created_id}"
        assert matching_sim.get('simable', {}).get('price') == '4.5', f"Price mismatch for ID {created_id}"

