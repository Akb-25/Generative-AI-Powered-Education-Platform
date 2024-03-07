from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms

from django.contrib.auth.models import AbstractUser

class UserProfile(User):
    full_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)