from django.shortcuts import render ,get_object_or_404, redirect
from categories.models import Categories
from posts.models import Post
from company.models import Company
from metadata.models import Metadata
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
def home(request):
    categories = Categories.objects.all()
    for category in categories:
        category.active_post_count = category.posts.filter(is_active=True).count()
        category.inactive_post_count = category.posts.filter(is_active=False).count()
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
    for post in posts:
        post.applicants_count = post.applicants.count()
    props={
        "posts":posts,
        "category":category_name,
    }
    return render(request , "posts.html",props)

def post(request):
    id = request.GET.get("id")
    post = Post.objects.get(id=id)
    user_is_applicant = request.user in post.applicants.all()
    print(user_is_applicant)
    props = {
        "post": post,
        "is_applicant": user_is_applicant
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
 
def search(request):
    query = request.GET.get('q')  
    print(query)
    if query:
        categories = Categories.objects.filter(Q(name__icontains=query))
    props = {
          "categories":categories
    }
    return render(request , "home.html",props)

def apply(request,id):
    url = f'/post?id={id}'
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to apply.')
        return redirect(url)  
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
        
@login_required
def upload_document(request):
    print(request.FILES.get('document'))
    if request.method == 'POST':
        user = request.user
        metadata = Metadata.objects.get_or_create(user=user)[0]
        file = request.FILES.get('document') 
        if file:
            metadata.document = file
            metadata.save()
            return redirect('profile')  

@login_required
def upload_profile_pic(request):
    if request.method == 'POST':
        file = request.FILES.get('profile_photo')
        user = request.user
        metadata = Metadata.objects.get_or_create(user=user)[0]
        file = request.FILES.get('profile_photo') 
        if file:
            metadata.profile_photo = file
            metadata.save()
            return redirect('profile')  

@login_required
def profile(request):
    metadata = Metadata.objects.get_or_create(user=request.user)[0]
    document_url = None
    profile_pic_url = None
    print("print", metadata.document , request.user)
    if metadata:
        document_url = settings.MEDIA_URL+ str(metadata.document)
        profile_pic_url = metadata.profile_photo.url if metadata.profile_photo else None
    props = {
        "document_url": document_url,
        "profile_pic_url":profile_pic_url
    }
    return render(request, "profile.html", props) 

def company(request):
    id = request.GET.get("id")
    company = Company.objects.get(id=id)
    posts = company.posts.all()
    props = {
        "company": company,
        "posts":posts
    }
    print(props)
    return render(request , "company.html" ,props)


    
    


        
        
        
        

        