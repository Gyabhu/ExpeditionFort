from django.urls import path
from .import views

urlpatterns = [
    path('', views.store , name= 'home'),
    path('category/',views.category, name = 'category'),
    path('product/',views.product, name = 'product'),
    path('cart/',views.cart, name = 'cart'),
    path('checkout/',views.checkout, name = 'checkout'),
    path('contact/',views.contact, name = 'contact'),
    path('login/',views.login, name = 'login'),
]