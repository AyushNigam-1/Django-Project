from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'company', 'location', 'posted_at', 'is_active', 'salary')
    list_filter = ('category', 'company', 'is_active', 'posted_at')
    search_fields = ('title', 'desc', 'location')
    date_hierarchy = 'posted_at'

admin.site.register(Post, PostAdmin)
