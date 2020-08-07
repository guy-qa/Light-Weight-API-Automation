from api_logic.pet_api import Pet

"""
*********************************************************************************************
  Author                  |   Muhammad Umair                                                    *
  Date Created            |   9/1/2019                                                      *
*********************************************************************************************
"""

pet = Pet()

def test_get_pet_by_status():
    """
        Description:
        |   This test case will get a pet by its availability status & checks the status of the response of API call
    """
    response = pet.find_pet_by_status('available')
    assert response.status_code == 200

def test_get_pet_by_id():
    """
        Description:
        |   This test case will get a pet by its ID & checks the status of the response of API call
    """
    response = pet.find_pet_by_id(1)
    assert response.status_code == 200

def test_post_add_new_pet():
    """
        Description:
        |   This test case will add a new pet to the store & checks the status of the response of API call
    """
    response = pet.add_new_pet('\\pet\\add_new_pet.json')
    assert response.status_code == 200

def test_put_update_existing_pet():
    """
        Description:
        |   This test case will update an existing pet in the store & checks the status of the response of API call
    """
    response = pet.update_pet('\\pet\\update_pet.json')
    assert response.status_code == 200

def test_delete_pet_by_id():
    """
        Description:
        |   This test case will delete an existing pet in the store & checks the status of the response of API call
    """
    response = pet.delete_pet_by_id(1)
    assert response.status_code == 200