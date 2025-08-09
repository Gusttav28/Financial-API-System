import pytest

from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db

@pytest.mark.parametrize("api_call", ["juan", "mary", "1"])
def test_financialapi(api_client, api_call):
    payload = dict(
        name = api_call  
    )
    
    response = api_client.post("/addItem/", payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == payload["name"]