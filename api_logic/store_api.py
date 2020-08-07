from common.utils import Utils
import requests

common_utils = Utils()

"""
*********************************************************************************************
  Author                  |   Muhammad Umair                                                     *
  Date Created            |   9/1/2019                                                      *
*********************************************************************************************
"""

class Store:
    """
        Description:
        |   This class contains methods for testing API calls for store endpoint
    """

    def __init__(self):
        """
            Description:
            |   This is the Constructor method for the class Store.
        """
        self.base_url = "https://petstore.swagger.io/v2"

    def find_inventory_status(self):
        """
            Description:
            |   This method will return pet inventory by status
            |   This method builds the request URL through utils method build_get_request_url()
            |   It then initiates a GET call & returns the response
        """
        endpoint = "/store/inventory"
        queryparam = ""
        request_url = common_utils.build_get_request_url(self.base_url, endpoint, queryparam)
        print(request_url)
        response = requests.get(request_url)
        print(response.content)
        return response

    def find_order_by_id(self, param):
        """
            Description:
            |   This method will find a pet purchase order by ID
            |   This method builds the request URL through utils method build_get_request_url(), for query paramaters recieved in param (number)
            |   It then initiates a GET call & returns the response
        """
        endpoint = "/store/order"
        queryparam = "/" + str(param)
        request_url = common_utils.build_get_request_url(self.base_url, endpoint, queryparam)
        print(request_url)
        response = requests.get(request_url)
        print(response.content)
        return response

    def add_new_pet_order(self, param):
        """
            Description:
            |   This method will place an order for purchasing a pet
            |   This method builds the request URL through utils method get_request_json(), for the json object recieved in param (string)
            |   It then initiates a POST call & returns the response
        """
        endpoint = "/store/order"
        request_url = self.base_url + endpoint
        print(request_url)
        request_json = common_utils.get_request_json(param)
        response = requests.post(request_url, json=request_json)
        print(response.content)
        return response

    def delete_order_by_id(self, param):
        """
            Description:
            |   This method will delete a pet purchase order from the store
            |   This method builds the request URL through utils method build_get_request_url(), for query parameters received in param (number)
            |   It then initiates a DELETE call & returns the response
        """
        endpoint = "/store/order"
        queryparam = "/" + str(param)
        request_url = common_utils.build_get_request_url(self.base_url, endpoint, queryparam)
        print(request_url)
        response = requests.delete(request_url)
        print(response.content)
        return response

