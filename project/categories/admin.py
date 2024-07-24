from django.contrib import admin
from categories.models import Categories
class CategoriesAdmin(admin.ModelAdmin):
    list_display=("name","counts","desc","icon")
    
admin.site.register(Categories , CategoriesAdmin)
