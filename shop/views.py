from distutils.log import error
import email
from itertools import product
from multiprocessing.sharedctypes import Value
from re import L
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password , check_password
from .models import Product, Orders,Contact, Customer
from math import ceil

from django.contrib import messages 
from django.contrib.auth.models import User 
#from django.validators import ValidationError
import json
 

from django.http import HttpResponse


# Create your views her

def index(request):
   

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        Prod = Product.objects.filter(category=cat)
        n = len(Prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([Prod, range(1, nSlides), nSlides])

   

    params = {'allProds':allProds}
    return render(request, 'shop/Index.html', params)


def about(request):
    return render(request, 'shop/About.html')

   

def productview(request, myid):
    product = Product.objects.filter(id=myid)
    
    return render(request, 'shop/productview.html',{'product':product[0]})   

    
#fetch items in cart 

def service(request):
    return render(request, 'shop/service.html')  

def search(request):
    return render(request, 'shop/search.html')  

#order detales
def checkout(request):
  
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')

        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address1','')
     
        city = request.POST.get('city','')
        state = request.POST.get('state','')
       
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
         
        Orders = Orders(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone = phone)
        Orders.save()
        thanks = True
        id = order_id
        #return HttpResponse("order")
        return render(request, 'shop/checkout.html',{'thank':thanks, 'id':id}) 
    return render(request, 'shop/checkout.html') 

def home(request):
    return render(request, 'shop/home.html') 

def validateCustomer(customer):
    error_message = None
    if(not customer.first_name):
        error_message = "First Name Required"
    elif len(customer.first_name) <4:
        error_message = "First Name must be 4 char required"


    if(not customer.last_name):
        error_message = "Last Name Name Required"
    elif len(customer.last_name) <4:
        error_message = "Last_name must be 4 char required"   


    if(not customer.phone):
        error_message = "Phone Name Name Required"
    elif len(customer.phone) <4:
        error_message = "Phone must be 4 char required" 

    if(not customer.email):
        error_message = "EmailName Name Required"
    elif len(customer.email) <4:
        error_message = "Email must be 4 char required" 


    if(not customer.password):
        error_message = "password Name Required"
    elif len(customer.password) <4:
        error_message = "password must be 4 char required"  
        
    elif customer.isExists():   
        error_message = 'Email Address Already Register...' 
    return error_message 

def registerUser(request):
    postData = request.POST   
    
    first_name = postData.get('first_name')
    last_name = postData.get('last_name')
        
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    value = {
        'first_name' : first_name,
        'last_name' : last_name,
        'phone' : phone,
        'password' : password,
        'email' : email,
        }
    error_message = None  

    print(first_name,last_name,phone,email ,password)
    customer = Customer(first_name= first_name,last_name= last_name,phone= phone,email= email, password= password)
    error_message = validateCustomer(customer)
       
    if not error_message:
           
        customer.password = make_password(customer.password) 
        customer.register()
        return render(request, 'shop/index.html')  
    else:
        data = {
            'error': error_message,
            'values': value,
            }        
        return render(request, 'shop/sng.html',data) 


def sng(request):
    if request.method == 'GET':
        return render(request, 'shop/sng.html')      
    else:
        return registerUser(request)  
   
def login(request):
    if request.method == 'GET': 
        return render(request, 'shop/login.html')  

    else:      
        email = request.POST.get('email')
        password = request.POST.get('password') 
        customer = Customer.get(email)
       
        print(customer)
        print(email,password)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect('/shop')
            else:
                error_message = 'Email or Password Invalid!'

        else:
            error_message = 'Email or Password Invalid!'
        return render(request,'shop/login.html',{'error': error_message})


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')

        print(request)
        print(name,email,phone,desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')

def policy(request):
    return render(request, 'shop/policy.html')
        

def exchange(request):
    return render(request, 'shop/exchange.html')


def term(request):
    return render(request, 'shop/term.html')

def payments(request):
    return render(request, 'shop/payments.html')


def cart(request):
   return render(request, 'shop/cart.html')    

'''
def cart(request):
   
    cart = request.session.get('cart', None)
    if not cart:
        cart = {}
        request.session['cart'] = cart
        ids = (list(cart.keys()))
        ids = (list(request.session.get('cart').keys()))
        item = product.pr(ids)

        order_id = order_id.objects.filter(user=request.user)

        print(item)

        return render(request, 'cart.html', {'items': item, 'addresses':order_id})    

'''





    