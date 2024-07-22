# Airalo Automation Project

## Overview

This project contains automation scripts for testing Airalo's API and UI functionalities. The project is structured into different modules for API and UI testing, with reusable components for base functionalities.

## Project Structure

```
airalo_automation_ilona/
├── api/
│   ├── init.py
│   ├── api_base.py
│   └── api_endpoints.py
│
├── base/
│   ├── init.py
│   ├── base_elements.py
│   └── base_page.py
│
├── pages/
│   ├── init.py
│   ├── home_page.py
│   └── japan_esim.py
│
├── source_shop/
│   ├── init.py
│   ├── data.py
│   └── locators.py
│
├── tests/
│   ├── test_api_automation.py
│   └── test_ui_automation.py
├── conftest.py
```


## Setup Instructions

### Prerequisites

- Python 3.9
- `pip` (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ilona-py/airalo_automation_ilona
    cd airalo_automation_ilona
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

### API Tests

To run the API test, use the following command:
```bash
pytest tests/test_api_automation.py 
```

### UI Tests

To run the UI test, use the following command:
```bash
pytest tests/test_ui_automation.py 
```

### Utilities

```
•	data.py: Contains data used in the tests.
•	locators.py: Contains element locators used in the page classes.
```


### API Test: test_api_automation

This test case aims to automate the process of creating an eSIM order via the Airalo Partner API and verifying the correctness and consistency of the response data. 
The approach is broken down into several key steps, each designed to ensure comprehensive coverage and validation of the API functionalities.

Approach:
```
1.	Setup and Authentication:
	•	Goal: Ensure the API client is authenticated and ready to make requests.
	•	Implementation:
	•	Use the api_endpoints.login() method to authenticate and obtain OAuth2 tokens.
	•	This step is crucial to gain access to the API endpoints.
2.	Order Creation:
	•	Goal: Create an eSIM order with a specified quantity and package ID.
	•	Implementation:
	•	Call the api_endpoints.post_submit_order(quantity, package_id) method with the required parameters.
	•	Store the response and extract the order details.
	•	This step tests the API’s ability to create orders and return the correct details.
3.	Verify Order Details:
	•	Goal: Ensure the order response contains the correct number of eSIMs and matches the requested package ID and quantity.
	•	Implementation:
	•	Verify the sims list length matches the specified quantity.
	•	Check that package_id and quantity in the response match the inputs.
	•	Assertions are used to confirm these details, ensuring the API processes orders correctly.
4.	Retrieve eSIM List:
	•	Goal: Fetch the list of eSIMs associated with the created order.
	•	Implementation:
	•	Call the api_endpoints.get_sims() method to get the list of eSIMs.
	•	Extract and store the relevant eSIM data for further verification.
5.	Verify eSIM Details:
	•	Goal: Check that each eSIM in the list has the correct properties and matches the order details.
	•	Implementation:
	•	Verify key attributes (id, code, currency, type, esim_type, validity, package, data, price, created_at, manual_installation, qrcode_installation, quantity, package_id) between the order response and the retrieved eSIM list.
	•	Ensure installation_guides match the expected URLs.
	•	These checks validate the consistency and accuracy of the eSIM details provided by the API.
6.	Check Each eSIM Information:
	•	Goal: Ensure consistency and correct sequencing of each eSIM’s data.
	•	Implementation:
	•	Verify that each eSIM ID is incremented by 1 from the previous eSIM.
	•	Ensure other properties (created_at, lpa, matching_id, apn_type, apn_value, is_roaming, direct_apple_installation_url) are consistent across all eSIMs.
	•	This step checks the integrity and ordering of eSIM data, which is critical for maintaining proper records.
7.	Check ICCID Uniqueness and Sequence:
	•	Goal: Ensure ICCID values are unique and increment sequentially.
	•	Implementation:
	•	Collect ICCID values from all eSIMs.
	•	Verify that each ICCID subsequent ICCID increments by 1.
	•	This ensures that the ICCIDs are properly assigned and unique, preventing potential conflicts or issues in eSIM identification.
```

By following this structured approach, the test case ensures thorough verification of the eSIM order creation process and the consistency of the returned data. 
The steps are designed to validate both the functional correctness of the API endpoints and the integrity of the eSIM data, providing confidence in the reliability and accuracy of the system.

### UI Test: test_ui_automation

This test case aims to automate the process of verifying the details of a specific eSIM package on the Japan eSIM store page. 
The approach is broken down into several key steps, each designed to ensure comprehensive coverage and validation of the UI functionalities and data correctness.


Steps:
```
1. Close advertising if visible: Ensure any advertising pop-ups are closed.
2. Search for Japan:
	 •	Accept cookies.
	 •	Click no on push notifications.
	 •	Search for Japan eSIM.
	 •	Verify the active tab is correctly displayed.
3. Select an eSIM Package: Click on the ‘Buy Now’ button for the first eSIM package.
4. Verify Package Details:
	 •	Check the eSIM operator title.
	 •	Verify the coverage area.
	 •	Check the data in GB.
	 •	Verify the validity period.
	 •	Check the price.
```

By following this structured approach, the test case ensures thorough verification of the eSIM package details on the Japan store page. 
The steps are designed to validate both the UI elements’ functionality and the accuracy of the displayed data, providing confidence in the reliability and correctness of the eSIM store page.
 

