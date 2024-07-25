from django.contrib import admin
from django.contrib import admin
from posts.models import Post
class PostsAdmin(admin.ModelAdmin):
    list_display=("category","location","desc","type","applicants","posted_at","is_active")
    
admin.site.register(Post , PostsAdmin)
# Register your models here.
