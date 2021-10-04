from typing import Container
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields

from .models import UserProfile

class UserCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('email',)

class UserChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('email',)
