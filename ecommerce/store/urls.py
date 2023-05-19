from django.urls import path
from .import views

urlpatterns = [
    path('', views.store, name= 'home'),
    path('category/', views.category, name = 'category'),
    path('product/', views.product, name = 'product'),
    path('product-detail/<int:id>', views.product_detail, name = 'product_detail'),
    path('cart/',views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('contact/', views.contact, name = 'contact'),
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),

]