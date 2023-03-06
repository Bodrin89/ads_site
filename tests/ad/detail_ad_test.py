import pytest

from ads.serializers import AdDetailSerializer
from tests.facrtories import AdFactory


@pytest.mark.django_db
def test_list_ad(client, access_token):
    ad = AdFactory.create()
    response_data = AdDetailSerializer(ad).data

    response = client.get(f"/ad/{ad.pk}/", HTTP_AUTHORIZATION="Bearer " + access_token)
    assert response.status_code == 200
    assert response.data == response_data
