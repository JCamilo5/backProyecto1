from django.contrib import admin

from .models import Enterprise, Management

# Register your models here.


admin.site.register([Enterprise, Management])
