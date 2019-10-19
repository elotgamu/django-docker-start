from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Modified form to create user in admin
    """

    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """Modified form to change user data in admin"""

    class Meta:
        model = User
        fields = ("username", "email")
