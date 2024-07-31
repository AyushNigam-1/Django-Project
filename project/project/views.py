from django.shortcuts import render , redirect
from categories.models import Categories
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
from django.contrib.auth.hashers import make_password

def home(request):
    categories = Categories.objects.all()
    props = {
        "categories" : categories
    }
    return render(request , "home.html",props)

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

def login_user(request):
    if request.method == 'POST': 
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        if not User.objects.filter(username = username).exists():
            messages.error(request , 'Please check username and password again')
            return render(request , 'login.html')

        user = authenticate(username=username , password = password)

        if user is None:
            messages.error(request , 'Please check email and password again')
            return render(request , 'login.html')
        else:
            login(request,user=user)
            return redirect('home')
    
    return render(request,'login.html')

def register(request):
    if request.method == 'POST': 
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(first_name)
        if User.objects.filter(email = email).exists():
            messages.error(request , 'Please try another email')
            return render(request , 'register.html')

        user = User(first_name=first_name,last_name=last_name,username=username, email=email , password = make_password(password))
        user.save()
        login(request,user=user)
        return redirect('home')
    
    return render(request,'register.html')