from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.detail, name='detail'),
    path('cart/', views.cart, name='cart'),
]