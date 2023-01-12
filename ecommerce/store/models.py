from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=400,unique = True)
    logo = models.CharField(blank=True,max_length=50)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=400, unique= True)
    def __str__(self):
        return self.name

class Carousel(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media', null= "True")
    description = models.TextField(blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media', blank=True)
    slug = models.CharField(max_length=40, unique=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

STOCK = (('In stock','In stock'), ('Out of stock', 'Out of Stock'))
LABELS = (('new','new'),('sale','sale'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='image/')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank= True )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank= True )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null = True)
    stock = models.CharField( choices= STOCK,blank = True, max_length=30)
    labels = models.CharField(choices= LABELS, blank = True, max_length=30)
    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE, null=True, blank= True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)


    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank = True)
    date_added = models.DateField(auto_now_add=True)

class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address