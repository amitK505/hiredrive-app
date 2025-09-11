"""
URL configuration for app1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from cool import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('/login/', views.home),
    path('signup/', views.signup , name='signup'),
    path('logout/', views.logout, name='logout'),
    path('', views.home ,name="home"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile ,name="profile"),
    path('feedback/', views.feedback ,name="feedback"),
    path('feedback/<str:feedbackid>/', views.practice ,name="practice"),
    path('go/', views.go,name='go'),
    path('home/',views.home),
    path('go/hiredetail/', views.hiredetail,name='hiredetail'),
    path('go/hiredetail/hiresearch', views.hiresearch,name='search2'),
    path('go/hiredetail/hireback', views.hireback,name='hireback'),
    path('hiredetail/', views.home),
    path('go/drivedetail/', views.drivedetail,name='drivedetail'),
    path('go/drivedetail/id/', views.drivedetail,name='drivedetail'),
    path('go/drivedetail/id/search', views.search,name='drivedetail'), 
    path('go/drivedetail/search/', views.search,name="search"),
    path('go/drivedetail/search/back', views.back,name="back"),
    path('go/drivedetail/back2', views.back2,name='back2'),
    path('go/drivedetail/id/back', views.back2),

    

   
    
]
