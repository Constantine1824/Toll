from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Custom Manager for User creation"""

    def create_user(self, email, password, **kwargs):
        """Creates a user with just the email"""
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,**kwargs)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,password, **kwargs):
        """Creates a new superuser"""
        kwargs.setdefault('is_staff',True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staff=True'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        return self.create_user(email,password,**kwargs)