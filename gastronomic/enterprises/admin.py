from django.contrib import admin

from .models import Enterprise, Management

# Register your models here.


#admin.site.register([Enterprise, Management])
@admin.register(Enterprise)
class enterprise(admin.ModelAdmin):
    list_display=('name','location','business_hours','status','created')
    list_filter=('status','business_hours','location',)
    search_fields=['name','location']
@admin.register(Management)
class management(admin.ModelAdmin):
    list_display=('date','status')
    list_filter=('status',)