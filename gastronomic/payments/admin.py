from django.contrib import admin

from .models import Payment

# Register your models here.

#admin.site.register(Payment)
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=('payment_type','payment_value','delivery')
    list_filter=('payment_type','delivery',)
    search_fields=('payment_type',)