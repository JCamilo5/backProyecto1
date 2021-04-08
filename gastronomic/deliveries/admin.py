from django.contrib import admin

from .models import Delivery, Courier

# Register your models here.


admin.site.register([Delivery, Courier])
