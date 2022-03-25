from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .models import *

import json

from .forms import AdminForm, CreateUserForm

# Create your views here.


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            
            messages.success(request, 'Account was created successfully ')
                
            return redirect('form')

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')

    return render(request, 'form.html')


def logoutUser(request):
    logout(request)
    return redirect('form')

@login_required(login_url='form')
@allowed_users(allowed_roles=['customer'])
def UserPage(request):
   
    if request.method == "POST":
        customer = request.user.customer.order_set.all()
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = ''

    carts = Image.objects.all()
    context = {'carts': carts, 'cartItems': cartItems}
    return render (request, 'user.html', context)




@login_required(login_url='form')
@allowed_users(allowed_roles=['admin', 'customer'])
def profilePage(request):
    users = request.user
    user = Customer.objects.all()


    if request.method == "POST":
        customer = request.user.customer.order_set.all()
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = ''

    context = {'users': users, 'user': user,'cartItems': cartItems}
    return render(request, 'profile.html', context)





@login_required(login_url='form')
@admin_only
def main(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = ['get_cart_items']

    carts = Image.objects.all()
    context = {'carts': carts, 'cartItems': cartItems}
    return render(request, 'index.html', context)


@login_required(login_url='form')
@allowed_users(allowed_roles=['admin', 'customer'])
def basket(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = ''
    
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'basket.html', context)


@login_required(login_url='form')
@allowed_users(allowed_roles=['admin', 'customer'])
def updateitem(request):
    data = json.loads(request.body)
    cartId = data['cartId']
    action = data['action']
    print('Action: ', action)
    print('CartId: ', cartId)


    customer = request.user.customer
    cart = Image.objects.get(id=cartId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem,created = OrderItem.objects.get_or_create(order=order, cart=cart)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)
    
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()
    

    return JsonResponse('Item added', safe=False)
