import pytest


@pytest.mark.django_db
def test_ad_create(client, access_token, user, category):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "Test_name_22",
        "price": 1111
    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Test_name_22",
        "price": 1111,
        "description": None,
        "image": None,
        "author": user.pk,
        "category": category.pk
    }
    response = client.post("/ad/create/", data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data
