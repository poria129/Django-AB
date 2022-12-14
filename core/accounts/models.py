from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import ugettext_lazy as _

# Create your models here.

"""
Custom user model manager where email is the unique identifiers
for authentication instead of usernames.
"""
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password
        and extra data.
        """
        if not email:
            raise ValueError(_('The email must be set'))
        
        email = self.normilize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password
        and extra data.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        pass


# castum model user for our app.
class User (AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_Staff = models.booleanField(default=False)
    is_active = models.booleanField(default=True)
    # is_verified = models.booleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email