from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max, Min

from django.http import HttpResponse


# Context Pre-processor
def categories(request):
    return {
        "categories": Category.objects.all(),
        "subcategories": SubCategory.objects.all(),
    }


def store(request):
    products = Product.objects.all()
    carousels = Carousel.objects.all()
    brands = Brand.objects.all()
    context = {"products": products, "carousels": carousels, "brands": brands}

    return render(request, 'store/index.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    subcategories = SubCategory.objects.all()
    products = Product.objects.filter(category=category)
    # For Price filter - getting max and min price for filtered category
    min_max_price = products.aggregate(Min('price'), Max('price'))

    context = {"products": products, "subcategories": subcategories, "category": category, 'pricefilter': min_max_price}
    return render(request, 'store/category.html', context)






def product_detail(request, id):
    product = Product.objects.get(id=id)
    products = Product.objects.all()
    print("This is error = ", product.labels)
    context = {"product": product, "products": products}
    return render(request, 'store/product-details.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.username
            messages.success(request, "Login Sucessful!")
            return render(request, 'store/index.html', {"name": name})


        else:
            messages.error(request, "Username or Password Does not match")
            return redirect('/signin')

    return render(request, 'store/login.html')


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
    return render(request, 'store/signup.html', context)


def signout(request):
    logout(request)
    messages.success(request, "Logged out Sucessfully!")
    return redirect('home')
