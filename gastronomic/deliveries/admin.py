from django.contrib import admin

from .models import Delivery

# Register your models here.


#admin.site.register(Delivery)
@admin.register(Delivery)
class deliveryAdmin(admin.ModelAdmin):
    list_display=('courier','order','status')
    list_filter=('status',)
    search_fields=('courier__email',)