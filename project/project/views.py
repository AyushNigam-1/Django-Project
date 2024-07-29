from django.shortcuts import render , redirect
from categories.models import Categories
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
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
    
    category_name = request.GET.get("category")
    category = Categories.objects.get(name = category_name)
    posts = Post.objects.all().filter(category = category)
    props={
        "posts":posts,
        "category":category_name,
    }
    return render(request , "posts.html",props)

def post(request):
    id = request.GET.get("id")
    post = Post.objects.get(id=id)
    props = {
        "post":post
    }
    print(props)
    return render(request , "post.html" ,props)

def login(request):
    if request.method == 'POST': 
        email = request.GET.get("email")
        password = request.GET.get("password")
       
        if not User.objects.filter(email = email).exists():
            messages.error(request , 'Please check email and password again')
            return render(request , 'login.html')

        user = authenticate(email=email , password = password)

        if user is None:
            messages.error(request , 'Please check email and password again')
            return render(request , 'login.html')
        else:
            login(user)
            return redirect('')
    
    return render(request,'login.html')