"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('index', views.index, name='index'),
    path('hom', views.hom, name="hom"),
    path('view', views.view, name='view'),
    path('add', views.add, name='add'),
    path('remove', views.remove, name='remove'),
    path('remove/<int:emp_id>', views.remove, name='remove'),
    path('filter', views.filter, name='filter'),
    path('filter/<int:emp_id>', views.filter, name='filter'),
    path('emp-list',views.empList, name="emp-list"),
    path('emp-detail/<str:pk>/',views.empDetail, name="emp-detail"),
    path('emp-create',views.empCreate, name="emp-create"),
    path('emp-update/<str:pk>',views.empUpdate, name="emp-update"),
    path('emp-delete/<str:pk>',views.empDelete, name="emp-delete")
]
