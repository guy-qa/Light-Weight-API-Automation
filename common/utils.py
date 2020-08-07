import json
from pathlib import Path

"""
*********************************************************************************************
  Author                  |   Muhammad Umair                                                    *
  Date Created            |   9/1/2019                                                      *
*********************************************************************************************
"""

class Utils:
    """
       Description:
       |   This class contains utility (helping) methods for testing API calls
    """

    def build_get_request_url(self, baseurl, endpoint, queryparam):
        """
            Description:
            |   This method builds a request URL by concatinating base URL, endpoint & query parameters strings recieved in
            |   variables baseurl , endpoint , queryparam respectively
        """
        self.request_url = baseurl+endpoint+queryparam
        return self.request_url

    def get_request_json(self, param):
        """
            Description:
            |   This method gets the required payload, stored as json object
            |   This method uses another method: get_project_root() that builds the path for the required json file, as recieved in param (string)
            |   It then opens the file to read & returns the request payload.
        """
        file_path = str(self.get_project_root()) + "\\payloads" + param
        file = open(file_path, 'r')
        json_input = file.read()
        request_json = json.loads(json_input)
        return request_json

    def get_project_root(self) -> Path:
        """
            Description:
            |   This method simply returns the path of the project root folder
        """
        return Path(__file__).parent.parent
