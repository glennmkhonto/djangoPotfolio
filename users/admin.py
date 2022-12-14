from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (('User Location', {'fields': ('location',)}),
        ('User Information', {'fields': ('email', 'user_name', 'first_name', 'date_of_birth', 'address', 'zip_code', 'city', 'start_date', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Bio', {'fields': ('about',)}),
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',
                       'date_of_birth', 'address', 'zip_code', 'city', 'start_date', 'photo')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
