from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Categories
from posts.models import Post
def home(request):
    categories = Categories.objects.all()
    props = {
        "categories" : categories
    }
    
    print(categories)
    return render(request , "home.html",props)
def auth(request):
    if request.method == 'POST':
        pass
    return render(request , "auth.html")

def posts(request):
    if request.method == 'POST':
        pass
    
    category = request.GET.get("category")
    print(category)
    category = Categories.objects.get(name = category)
    posts = Post.objects.all().filter(category = category)
    # print(posts)
    props={
        "posts":posts
    }
    return render(request , "posts.html",props)
    