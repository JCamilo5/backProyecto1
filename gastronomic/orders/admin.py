from django.contrib import admin

from .models import Order, Detail

# Register your models here.


admin.site.register([Order, Detail])
