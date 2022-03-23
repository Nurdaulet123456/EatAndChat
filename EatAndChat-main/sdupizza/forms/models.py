from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=25, null=True)



    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()

        total = sum([item.get_total for item in orderitems])

        return total


    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()

        total = sum([item.quantity for item in orderitems])

        return total


class Form(models.Model):
    user_name = models.CharField(max_length=400)
    city = models.CharField(max_length=500)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name + ' ' + self.phone


class Image(models.Model):
    img = models.ImageField(null = True, blank = True)
    img_name = models.CharField(max_length=400)
    img_subtitle = models.TextField(max_length=10000)
    img_price = models.FloatField()


    def __str__(self):
        return self.img_name
    

    @property
    def imageUrl(self):
        try:
            url = self.img.url
        except:
            url = ''
        
        return url


class Stock(models.Model):

    img = models.ImageField()
    img_name = models.CharField(max_length=400)
    img_subtitle = models.TextField(max_length=10000)


    def __str__(self):
        return self.img_name


class OrderItem(models.Model):
    cart = models.ForeignKey(Image, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.cart.img_price * self.quantity

        return total


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address