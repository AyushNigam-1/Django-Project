"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project import views  
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home" ),
    path('posts', views.posts,name='posts' ),
    path('post', views.post,name='post' ),
    path('login', views.login_user,name='login' ),
    path('register', views.register,name='register' ),
    path('logout', views.logout_user,name='logout' ),
    path('apply/<int:id>/', views.apply,name='apply' ),
    path('createpost/<int:id>', views.createpost,name='createpost' ),
    path('profile', views.profile,name='profile' ),
    path('upload', views.upload_document,name='upload' ),
    path('search', views.search,name='search' ),
    path('company', views.company,name='company' ),
    path('upload_profile_pic', views.upload_profile_pic,name='upload_profile_pic' ),
]

def custom_404(request, exception):
    return render(request, 'error.html', status=404)

handler404 = custom_404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)