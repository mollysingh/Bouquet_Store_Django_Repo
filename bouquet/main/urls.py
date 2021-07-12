from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('cart/',views.cart,name="cart"),
    path('cart/remove/',views.removefromcart,name="remove"),
    path('cart/checkout/',views.loginUser,name="login"),
    path('cart/checkout/login',views.checkout,name="checkout"),
    path('cart/checkout/place/', views.placeOrder, name='place_order'),
    path('search_product',views.search_product,name="search_product"),
  
]
