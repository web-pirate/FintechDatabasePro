from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Override AbstractUser Variables
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # Declare Email as new PK 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    # Use __str__ method to make the User Object more Readable/Easier to work with
    def __str__(self):
        return self.username
