
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('accounts/profile/', views.profile, name='profile')
]
