from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "location","get_all_posts", "desc", "phone_number", "email", "fb_id", "ld_id", "x_id", "ig_id")
    
    def get_all_posts(self, obj):
        return ", ".join([str(post.id) for post in obj.posts.all()]) if obj.posts.exists() else "No Posts"
    get_all_posts.short_description = 'All Posts'

admin.site.register(Company, CompanyAdmin)
