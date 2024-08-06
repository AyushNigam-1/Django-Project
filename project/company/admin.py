from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'email', 'phone_number')
    list_filter = ('location',)
    search_fields = ('name', 'desc', 'location', 'email', 'phone_number')

admin.site.register(Company, CompanyAdmin)

