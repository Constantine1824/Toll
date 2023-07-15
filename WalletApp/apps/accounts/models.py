from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid

class UUIDModelField(models.Model):
    id = models.UUIDField(default=uuid.uuid4(),editable=False, primary_key=True)
    date_added = models.DateTimeField(auto_created=True,editable=False)
    date_edited = models.DateTimeField(auto_now_add=True,editable=False)

    class Meta:
        abstract= True

class User(AbstractBaseUser):
    email = models.EmailField(_('email_address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_created=True)

    objects = UserManager()
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'email'


class UserProfile(UUIDModelField):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    ip_address = models.IPAddressField() #Might use this later

# Create your models here.
