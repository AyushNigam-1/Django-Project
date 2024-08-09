from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Metadata  # Import your Metadata model

# Define an inline admin descriptor for the Metadata model
class MetadataInline(admin.StackedInline):
    model = Metadata
    can_delete = False

# Define a new User admin with the Metadata inline
class UserAdmin(BaseUserAdmin):
    inlines = (MetadataInline,)

# Unregister the original User admin and register the new User admin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
