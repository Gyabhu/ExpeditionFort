from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {}
    return render(request,'store/index.html', context)

def category(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,'store/category.html', context)
def category_male(request):
    products = Product.objects.all()
    context = {"products":products}
    return render (request, 'store/category-male.html', context)
def category_female(request):
    products = Product.objects.all()
    context = {"products":products}
    return render (request, 'store/category-female.html', context)

def category_gears(request):
    products = Product.objects.all()
    context = {"products":products}
    return render (request, 'store/category-gears.html', context)
def product(request):
    context = {}
    return render(request,'store/product.html', context)
def productdetail(request):
    context = {}
    return render(request,'store/product-details.html', context)
def cart(request):
    context = {}
    return render(request,'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html', context)

def contact(request):
    context = {}
    return render(request,'store/contact.html', context)

def login(request):
    context = {}
    return render(request,'store/login.html', context)
