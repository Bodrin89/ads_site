
import pytest
from faker import Faker

from tests.facrtories import UserFactory


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "User_test"
    password = "1234"
    role = "admin"
    email = Faker("ru_RU").email()

    django_user_model.objects.create_user(username=username, password=password, role=role, email=email)

    response = client.post('/user/token/', {"username": username, "password": password},
                           content_type="application/json")
    return response.data["access"]
