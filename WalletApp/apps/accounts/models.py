from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils.timezone import now
import random
from datetime import timedelta

class UUIDModelField(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),editable=False, primary_key=True)
    date_added = models.DateTimeField(auto_now_add=True,editable=False)
    date_edited = models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        abstract= True

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'accounts'

    def __str__(self):
        return self.email


class UserProfile(UUIDModelField):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=15)
    number_verified = models.BooleanField(default=False)
    last_name = models.CharField(max_length=20)
    ip_address = models.GenericIPAddressField(null=True) #Might use this later

    class Meta:
        app_label = 'accounts'

    def __str__(self):
        return f'{self.user}'
    
class OneTimeCode(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def generate_random_code(self):
        self.code = random.randint(100_00, 999_999)
        return self.code

# Create your models here.
