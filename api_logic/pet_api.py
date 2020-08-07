from common.utils import Utils
import requests

common_utils = Utils()

"""
*********************************************************************************************
  Author                  |   Muhammad Umair                                                     *
  Date Created            |   9/1/2019                                                      *
*********************************************************************************************
"""

class Pet:
    """
        Description:
        |   This class contains methods for testing API calls for pet endpoint
    """

    def __init__(self):
        """
            Description:
            |   This is the Constructor method for the class Pet.
        """
        self.base_url = "https://petstore.swagger.io/v2"

    def find_pet_by_status(self, param):
        """
            Description:
            |   This method will find a pet by its availability status -- Available values : available, pending, sold
            |   This method builds the request URL through utils method build_get_request_url(), for query paramaters recieved in param (string)
            |   It then initiates a GET call & returns the response
        """

        endpoint = "/pet/findByStatus"
        queryparam = "?status=" + param
        request_url = common_utils.build_get_request_url(self.base_url, endpoint, queryparam)
        print(request_url)
        response = requests.get(request_url)
        return response

    def find_pet_by_id(self, param):
        """
            Description:
            |   This method will find a pet by its ID
            |   This method builds the request URL through utils method build_get_request_url(), for query paramaters recieved in param (number)
            |   It then initiates a GET call & returns the response
        """
        endpoint = "/pet"
        queryparam = "/" + str(param)
        request_url = common_utils.build_get_request_url(self.base_url, endpoint, queryparam)
        print(request_url)
        response = requests.get(request_url)
        print(response.content)
        return response

    def add_new_pet(self, param):
        """
            Description:
            |   This method will add a new pet to the store.
            |   This method builds the request URL through utils method get_request_json(), for the json object recieved in param (string)
            |   It then initiates a POST call & returns the response
        """
        endpoint = "/pet"
        request_url = self.base_url + endpoint
        print(request_url)
        request_json = common_utils.get_request_json(param)
        response = requests.post(request_url, json=request_json)
        print(response.content)
        return response

    def update_pet(self, param):
        """
            Description:
            |   This method will update an existing pet
            |   This method builds the request URL through utils method get_request_json(), for the json object received in param (string)
            |   It then initiates a PUT call & returns the response
        """
        endpoint = "/pet"
        request_url = self.base_url + endpoint
        print(request_url)
        request_json = common_utils.get_request_json(param)
        response = requests.put(request_url, json=request_json)
        print(response.content)
        return response

    def delete_pet_by_id(self, param):
        """
            Description:
            |   This method will delete a pet from the store
            |   This method builds the request URL through utils method build_get_request_url(), for query parameters received in param (number)
            |   It then initiates a DELETE call & returns the response
        """
        endpoint = "/pet"
        queryparam = "/" + str(param)
        request_url = common_utils.build_get_request_url(self.base_url, endpoint, queryparam)
        print(request_url)
        response = requests.delete(request_url, headers={'api_key': 'special-key'})
        print(response.content)
        return response

