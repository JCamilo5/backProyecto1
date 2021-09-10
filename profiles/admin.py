from django.contrib import admin
from django.db import models

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    exclude = ("last_login", )
    class meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
