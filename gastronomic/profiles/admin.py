from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = UserProfile
    exclude = ("last_login", 'username')
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'type',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','enterprise')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(UserProfile, UserProfileAdmin)
