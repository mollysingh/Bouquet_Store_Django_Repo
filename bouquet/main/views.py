from main.models import Contact
from django.shortcuts import render,redirect
from datetime import datetime
from main.models import Contact,Product,Order
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.
def cartItems(cart):
    items=[]
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items

def priceCart(cart):
    cart_items=cartItems(cart)
    price=0
    for item in cart_items:
        price += item.price
    return price

def index(request):
    if 'cart' not in request.session:
        request.session['cart']=[]
    cart=request.session['cart']
    request.session.set_expiry(0)
    store_items=Product.objects.all()
    context={'store_items':store_items,'cart_size':len(cart)}

    if request.method=="POST":
        cart.append(int(request.POST['obj_id']))
        messages.success(request, 'Item added to Cart!')
        return redirect('home')
    
    return render(request,"index.html",context)

def cart(request):
    cart=request.session['cart']
    request.session.set_expiry(0)
    ctx={'cart':cart,'cart_size':len(cart),'cart_items':cartItems(cart),'total_price':priceCart(cart)}
    return render(request,"cart.html",ctx)

def removefromcart(request):
    request.session.set_expiry(0)
    obj_to_remove = (request.POST['obj_id'])
    s=obj_to_remove.replace('/','')
    obj_index = request.session['cart'].index(int(s))
    request.session['cart'].pop(obj_index)
    return redirect('cart')

def about(request):
     return render(request,"about.html")



def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    
    
    return render(request,"contact.html")

def checkout(request):
    
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart':cart, 'cart_size':len(cart), 'cart_items':cartItems(cart), 'total_price': priceCart(cart)}
    return render(request, "checkout.html", ctx)


def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        #check credentials
        User = authenticate(request,username=username, password=password)
        if User is not None:
            # A backend authenticated the credentials
            login(request,User)
            # cart = request.session['cart']
            # request.session.set_expiry(0)
            # context = {'cart':cart, 'cart_size':len(cart), 'cart_items':cartItems(cart), 'total_price': priceCart(cart)}
            return redirect('/cart/checkout/login')
            
        else:
            # No backend authenticated the credentials
            messages.warning(request, 'Invalid Credentials!!')
            return render(request,"login.html")

    return render(request,"login.html")

def genItemsList(cart):
    cart_items = cartItems(cart)
    items_list = ""
    for item in cart_items:
        items_list += ","
        items_list += item.name
    return items_list

def placeOrder(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart':cart, 'cart_size':len(cart), 'cart_items':cartItems(cart), 'total_price': priceCart(cart)}
    if request.method=="POST":
        order = Order()
        order.items = genItemsList(cart)
        order.first_name = request.POST.get('first_name')
        order.last_name = request.POST.get('last_name')
        order.address = request.POST.get('address')
        order.city = request.POST.get('city')
        order.payment_data = request.POST.get('payment_data')
        order.payment_method = request.POST.get('payment')
        
        
        order.save()
        request.session['cart'] = []
    return render(request, "place_order.html")

def search_product(request):
    if request.method=="POST":
        searched=request.POST['searched']
        products=Product.objects.filter(name__icontains=searched)
        return render(request,"search_product.html",{'searched':searched,'products':products})
            
              
    else:
         return render(request,"search_product.html")






   


  