import pytest


@pytest.mark.django_db
def test_selection_create(client, access_token, ad, user):
    data = {
        "items": ad.pk,
        "name": "test_name",
        "owner": user.pk
    }

    expected_data = {
        "items": [ad.pk],
        "name": "test_name",
        "owner": user.pk
    }

    response = client.post('/selection/create/', data, HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 201
    assert response.data == expected_data

