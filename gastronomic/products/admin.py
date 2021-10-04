from django.contrib import admin

from .models import Product, Image

# Register your models here.


#admin.site.register(Image)
@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display=('name','price','ingredients','enterprise')
    list_filter=('price','estimated_time')
    search_fields=('name','price')

@admin.register(Image)
class ImagenAdmin(admin.ModelAdmin):
    list_display=('url','product')