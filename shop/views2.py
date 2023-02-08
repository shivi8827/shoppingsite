from distutils.log import error
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





   

 

def sng(request):
    if request.method == 'GET':

        return render(request, 'shop/sng.html')      
        
    else:
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



      
        print(first_name,last_name,phone,email ,password)
        customer = Customer(first_name= first_name,last_name= last_name,phone= phone,email= email ,password= password)
        error_message = None

        if(not first_name):
            error_message = "First Name Required"
        elif len(first_name) <4:
            error_message = "First Name must be 4 char required"


        if(not last_name):
            error_message = "Last Name Name Required"
        elif len(last_name) <4:
            error_message = "Last_name must be 4 char required"   


        if(not phone):
            error_message = "Phone Name Name Required"
        elif len(phone) <4:
            error_message = "Phone must be 4 char required" 

        if(not email):
            error_message = "EmailName Name Required"
        elif len(email) <4:
            error_message = "Email must be 4 char required" 


        if(not password):
            error_message = "password Name Required"
        elif len(password) <4:
            error_message = "password must be 4 char required"  
        
        elif customer.isExists():   
            error_message = 'Email Address Already Register...' 
       




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

        


        
def login(request):
    return render(request, 'shop/login.html')
     


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


    

     


        

def logout(request):
    return render(request, 'shop/logout.html')  

