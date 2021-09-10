from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('posts/', postsView.as_view(), name="posts_view"),
]