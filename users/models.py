from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    """Model definition for User."""

    title = models.CharField(max_length=100)
    verification_token = models.TextField()
    phone_number = PhoneNumberField()

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'
