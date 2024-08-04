from django.shortcuts import render ,get_object_or_404, redirect
from categories.models import Categories
from posts.models import Post
from company.models import Company
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
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

def logout_user(request):
    logout(request)
    return redirect('home')


def createpost(request,id):
    if request.method == 'POST':
        title = request.POST.get("title")
        category_name = request.POST.get("category")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        salary = request.POST.get("salary")
        category = Categories.objects.get(name = category_name)
        company = Company.objects.get(id = id)
        if not location:
            location = company.location
        try:
            post = Post(title=title,category=category,company=company,location = location,salary=salary,desc=desc)
            post.save()
        except Exception :
            messages.error(request , 'Something went wrong , Please try again !')
        else:
            messages.success(request, 'Your data has been processed successfully!')
            url = f"posts/?category={category_name}"
            return redirect(url)
        
        return render(request,"createpost")
    
    
def apply(request,id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        try:
            post.applicants.add(request.user)
            post.save()
        except:
            messages.error(request , 'Something went wrong , Please try again !')
        else:
            messages.success(request, 'Your data has been processed successfully!')
            url = f'post/id={id}'
            return redirect(url)
            
    cv_url = request.user.resume_url
    props={
        "url":cv_url,
        "id":id 
        }
    return render(request , "apply.html",props)


        

    
    


        
        
        
        

        