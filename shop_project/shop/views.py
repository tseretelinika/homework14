from django.shortcuts import render
from .models import Product, Cart


def home(request):

    return render(request, 'shop/home.html')


def products(request):
    all_products = Product.objects.all()

    return render(request, 'shop/products.html', {'products': all_products})


def detail(request, id):
    product = Product.objects.get(id=id)

    return render(request, 'shop/detail.html', {'product': product})


def cart(request):
    user_cart = Cart.objects.filter(user=request.user).first()

    return render(request, 'shop/cart.html', {'cart': user_cart})
