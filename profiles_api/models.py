from django.db import models
## then add required models for overriding the standard django authentication
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
##########

## import to manage our alternative user authentication
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db) ## specify the database to save to

        return user

    def create_superuser(self, email, name, password):
        """Create anew superuser with given data"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff =True
        user.save(using=self._db) ## specify the database to save to

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retreive full name of user """
        return self.name

    def get_short_name(self):
        """Retreive sort name of user"""
        return self.name

    def __str__(self):
        """Retuen string representation of model"""
        return self.email
