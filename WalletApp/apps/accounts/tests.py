import pytest
import pytest_django
from .models import User
from .models import UserProfile
from django.urls import reverse

class TestAccountModels:
    @pytest.mark.django_db
    def testCreateUser(self):
        user = User.objects.create_user(email='ayomidet905@gmail.com', password='random')
        assert user.email == 'ayomidet905@gmail.com'
        assert user.password != 'random' # password should hash
        assert user.is_active == True
        assert user.is_staff == False

    @pytest.mark.django_db
    def testCreateSuperUser(self):
        user = User.objects.create_superuser(email='ayomidet905@gmail.com', password='another@random')
        assert user.email == 'ayomidet905@gmail.com'
        assert user.password != 'another@random'
        assert user.is_active == True
        assert user.is_superuser == True 

    @pytest.mark.django_db
    def testCreateProfile(self):
        user = User.objects.create_user(email='ayomide@cham.com', password='random')
        profile = UserProfile.objects.create(user=user,first_name='Ayo', last_name='Taiwo')
        profile.save()
        assert profile.user == user
        assert profile.id != 1
        assert profile.first_name == 'Ayo'


class TestAccountViews:

    @pytest.mark.django_db
    def testCreateUserView(self,client):
        data = {
            "email" : "ayomidet905@gmail.com",
            "password" : "Constantine_",
            "re_password" : "Constantine_"
        }
        url = reverse('user-list')
        resp = client.post(url,data=data)
        print(resp.json())
        assert User.objects.get(email='ayomidet905@gmail.com') is not None
        assert resp.status_code == 201

    @pytest.mark.django_db
    def testLoginandRefreshView(self,client,create_user):
        user = create_user(email='kanyin@gmail.com')
        user.set_password('JohnDoe@12')
        user.save()
        print(User.objects.get(email='kanyin@gmail.com').password)
        data = {
            'email': 'kanyin@gmail.com',
            "password" : "JohnDoe@12"
        }
        url = reverse('jwt-create')
        resp = client.post(url,data=data)
        print(resp.json())
        assert resp.status_code == 200
        assert 'access' in resp.json()
        assert 'refresh' in resp.json()
        url2 = reverse('jwt-refresh')
        resp2 = client.post(url2, data= {
            "refresh" : resp.json()['refresh']
        })
        assert 'access' in resp2.json()
