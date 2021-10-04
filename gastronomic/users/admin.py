from django.contrib import admin

from .models import Contact

# Register your models here.


#admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('lastnames','names','telephone','license_plate')
    list_filter=('location',)
    search_fields=('names','lastnames')