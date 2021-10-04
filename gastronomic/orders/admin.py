from django.contrib import admin

from .models import Order, Detail

# Register your models here.


#admin.site.register([Order, Detail])
@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    list_display=('date','status','location','client')
    list_filter=('date','status',)
    search_fields=('location','cliente__email')

@admin.register(Detail)
class detailAdmin(admin.ModelAdmin):
    list_display=('quantity','product','order')
    list_filter=('product__name',)
    search_fields=('product__name',)
