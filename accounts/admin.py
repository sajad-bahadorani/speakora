from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_active',
    )

    list_filter = ('role', 'is_active', 'is_staff')

    search_fields = ('username', 'email', 'first_name', 'last_name')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('role', 'phone_number', 'profile_picture')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'Updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')