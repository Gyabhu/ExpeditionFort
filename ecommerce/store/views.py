from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse



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

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            name = user.username
            messages.success(request,"Login Sucessful!")
            return render(request,'store/index.html',{"name": name})


        else:
            messages.error(request,"Username or Password Does not match")
            return redirect('/signin')


    return render(request,'store/login.html')
def signup(request):

    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'The email is already taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                messages.success(request, "Account Created sucessfully!")
                return redirect('/signin')
        else:
            messages.error(request, 'Password does not match')
    context = {}
    return render(request,'store/signup.html', context)
def signout(request):
    logout(request)
    messages.success(request,"Logged out Sucessfully!")
    return redirect('home')