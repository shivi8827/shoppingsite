from re import L
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password , check_password
from .models import Product, Contact, Orders, Customer
from math import ceil

from django.contrib import messages 
from django.contrib.auth.models import User 
#from django.validators import ValidationError

 

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
    
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name, email, phone, desc)
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')  

def service(request):
    return render(request, 'shop/service.html')  


def search(request):
    return render(request, 'shop/search.html')  
def productview(request, myid):
    product = Product.objects.filter(id=myid)
    
    return render(request, 'shop/productview.html',{'product':product[0]})  

def checkout(request):
     if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address1','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
    
        order = Orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone)
        order.save()
   
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
            error_message = "Last Name Required"
    elif len(customer.first_name) <4:
            error_message = "Last Name must be 4 char required"  

    if(not customer.phone):
            error_message = "phone Name Required"
    elif len(customer.phone) <4:
            error_message = "Phone Name must be 4 char required" 

    if(not customer.password):
            error_message = "Password Name Required"
    elif len(customer.password) <4:
            error_message = "Password Name must be 8 char required"

    if(not customer.email):
            error_message = "Email Name Required"
    elif len(customer.email) <8:
            error_message = "Email Name must be 8 char required"

    elif customer.isExists():   
            error_message = 'Email Address Already Register...' 
    return error_message



def sng(request):
    print(request.method)
    postData = request.POST   
    
    first_name = postData.get('first_name')
    last_name = postData.get('lastname')
        
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

    customer = Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
    error_message = validateCustomer(customer)
    print("cos",customer)
    messages.success(request, "Successfully Singup")
       

    if not error_message:
        customer.password = make_password(customer.password)
           
        customer.save()
        return redirect('/shop')
    else:
        data = {
            'error': error_message,
            'values': value,
            }    
        


        return render(request, 'shop/sng.html')  


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


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
     


        

def logout(request):
    return render(request, 'shop/logout.html')  



