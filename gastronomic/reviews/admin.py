from django.contrib import admin

from .models import Review

# Register your models here.


#admin.site.register(Review)
@admin.register(Review)
class reviewAdmin(admin.ModelAdmin):
    list_display=('quality_service','date','comments','order')
    list_filter=('date','quality_service',)
    search_fields=('presentation','preparation',)
    