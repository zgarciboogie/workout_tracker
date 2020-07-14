from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('products/', views.ProductList.as_view(), name='products-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('excersises/', views.ExcersiseList.as_view(), name='excersise-list'),
    path('excersises/<int:pk>', views.ExcersiseList.as_view(), name='excersise-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)