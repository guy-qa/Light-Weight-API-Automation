from api_logic.store_api import Store

"""
*********************************************************************************************
  Author                  |   Muhammad Umair                                                     *
  Date Created            |   9/1/2019                                                      *
*********************************************************************************************
"""

store = Store()

def test_get_inventory_by_status():
    """
        Description:
        |   This test case will get the inventory status of the store & checks the status of the response of API call
    """
    response = store.find_inventory_status()
    assert response.status_code == 200

def test_get_order_by_id():
    """
        Description:
        |   This test case will find an existing order in the store & checks the status of the response of API call
    """
    response = store.find_order_by_id(1)
    assert response.status_code == 200

def test_post_new_pet_order():
    """
        Description:
        |   This test case will put an order for a pet in the store & checks the status of the response of API call
    """
    response = store.add_new_pet_order('\\store\\pet_order.json')
    assert response.status_code == 200

def test_delete_order_by_id():
    """
        Description:
        |   This test case will delete an existing store order & checks the status of the response of API call
    """
    response = store.delete_order_by_id(1)
    assert response.status_code == 200