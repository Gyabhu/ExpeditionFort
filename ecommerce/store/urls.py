from django.urls import path
from .import views

urlpatterns = [
    path('', views.store , name= 'home'),
    path('category/',views.category, name = 'category'),
    path('product/',views.product, name = 'product'),
    path('productdetail/',views.productdetail, name = 'productdetail'),
    path('cart/',views.cart, name = 'cart'),
    path('checkout/',views.checkout, name = 'checkout'),
    path('contact/',views.contact, name = 'contact'),
    path('login/',views.login, name = 'login'),
    path('category-men/',views.category_male, name = 'category-men'),
    path('category-women/',views.category_female, name = 'category-women'),
    path('bags-gears/',views.category_gears, name = 'bags-gears'),

]