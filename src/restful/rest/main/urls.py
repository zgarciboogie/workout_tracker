from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='products-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)