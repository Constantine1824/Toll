from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils.timezone import now

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


class UserProfile(UUIDModelField):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    ip_address = models.GenericIPAddressField(null=True) #Might use this later

    class Meta:
        app_label = 'accounts'

# Create your models here.
