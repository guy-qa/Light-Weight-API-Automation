Requirements:
    This project requires the following packages to run
    1. Python
    2. Pytest
    3. Pytest-html
    4. Requests
    5. Json

Folder Structure:
    1. api_logic
            - This folder will contain all the API call logic files

                1. "pet_api.py" file contains the API methods for pet endpoint
                2. "store_api.py" file contains the API methods for store endpoint
    2. common
            - This folder contains logic files for utility methods

                1. "utils.py" contains utility (helping) methods for testing API calls
    3. payloads
            - This folder contains json files for POST / PUT request payloads

                1. "pet" folder contains the json files for POST/PUT requests payloads for pet endpoint
                    1. The "add_new_pet.json" file contains the payload for "test_post_add_new_pet" test case
                    2. The "update_pet.json" file contains the payload for "test_put_update_existing_pet" test case

                2. "store" folder contains the json files for POST/PUT requests payloads for store endpoint
                    1. The "pet_order.josn" file contains the payload for "test_post_new_pet_order" test case
    4. TestCases
            -  This folder contains the test cases for the "API Automation Challenge"

                1. "test_pet_api.py" file contains test cases for pet endpoint
                2. "test_store_api.py" file contains test cases for store endpoint
    5. TestReports
            - This folder contains test reports for each of the test files in html format, that can be easily viewed in the browser
                1. “PetTestreport.html” contains the test report in html format for “test_pet_api.py” tests
	            2. “StoreTestreport.html” contains the test report in html format for “test_store_api.py” tests
