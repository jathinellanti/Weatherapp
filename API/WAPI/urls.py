"""
URL configuration for klu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='WAPI-home'),
    path('forecast/', views.forecast, name='WAPI-forecast'),
    path('home/', views.home, name='WAPI-home'),
    path('home/forecast/', views.forecast, name='WAPI-forecast'),
    path('mumbai/', views.mumbai, name='WAPI-mumbai'),
    path('delhi/', views.delhi, name='WAPI-delhi'),
    path('bangalore/', views.bangalore, name='WAPI-bangalore'),
    path('kolkata/', views.kolkata, name='WAPI-kolkata'),
]



