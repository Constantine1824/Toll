import pytest
import pytest_django
from .models import User
from .models import UserProfile


class TestAccounts:
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
