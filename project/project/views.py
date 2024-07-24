from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Categories
def home(request):
    categories = Categories.objects.get()
    props = {
        "categories" : categories
    }
    print(categories)
    return render(request , "home.html",props)
def auth(request):
    if request.method == 'POST':
        pass
    return render(request , "auth.html")
def getcategories(request):
    categories = Categories.objects.get()
    return
    