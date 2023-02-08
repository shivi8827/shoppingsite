
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('products<int:myid>', views.productview, name="productview"),


   #path('products/<int:id>', views.products, name="products"),
   #path('validateCustomer/', views.validateCustomer, name="validateCustomer"),
   #path('registerUser/', views.registerUser, name="registerUser"),
    path('home/', views.home, name="home"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.login, name="login"),
    path('service/', views.service, name="service"),
   
    path('sng/', views.sng, name="sng"),
    path('policy/', views.policy, name="policy"),
    path('exchange/', views.exchange, name="exchange"),
    path('contact/', views.contact, name="contact"),
    path('term/', views.term, name="term"),
    path('payments/', views.payments, name="payments"),
    path('cart/', views.cart, name="cart"),
    
    #path('handleSignUp/', views.handleSignUp, name="handleSignUp"),

] 