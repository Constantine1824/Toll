import pytest
from apps.accounts.models import User
from rest_framework.test import APIClient

@pytest.fixture
def create_user(django_user_model,db):
    def create(**kwargs):
        return django_user_model.objects.create(**kwargs)
    return create

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def token():
    user = create_user(email='random@example.com', password='random12')
    resp = client.post()