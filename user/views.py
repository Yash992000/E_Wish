from django.shortcuts import get_object_or_404, redirect,render
from django.http import HttpResponse
from merchant.models import product
from auth_app.models import user
from user.models import Cart,CartItems
from django.db.models import Avg
from django.http import JsonResponse
import json

#from auth_app.forms import UserRegistrationForm  
#from auth_app.models import user_registration  

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# def cart(request):
#     return render(request,'cart.html')

# def checkout(request):
#     return render(request,'checkout.html')

def contact_us(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def gallery(request):
    obj = product.objects.filter(isApproved = True)
    return render(request,'gallery.html',{'image' : obj})

# def my_account(request):
#     return render(request,'my_account.html')

# def shop_detail(request):
#     return render(request,'shop_detail.html')

def shop(request):
    obj = product.objects.filter(isApproved = True)
    for prod in obj:
        ratings = prod.ratings_set.all().aggregate(Avg('productRating'))
        prod.average_rating = ratings['productRating__avg']
    return render(request,'shop.html',{'product' : obj})


# def shop(request):
#     if request.user.is_authenticated:
#         obj = product.objects.filter(isApproved = True)
#         #user = request.user
#         obj1 = get_object_or_404(user)
#         cart, created = Cart.objects.get_or_create(user = obj1,completed = False)
#         cartitems = cart.cartitems_set.all()
#         for prod in obj:
#             ratings = prod.ratings_set.all().aggregate(Avg('productRating'))
#             prod.average_rating = ratings['productRating__avg']
#         return render(request,'shop.html',{'product' : obj,'cart':cart,'cartitems' : cartitems})


# def wishlist(request):
#     return render(request,'wishlist.html')

# def userlogout(request):
#     try:
#         del request.session['username'] 
#         del request.session['email'] 
#         del request.session['contact'] 
#         del request.session['shopName'] 
#         del request.session['shopAddr'] 
#         del request.session['shopPhone'] 
#         return render(request,'login.html')
#     except Exception as e:
#         return HttpResponse(e)
#     return render(request,'merchant_login.html')

def add_to_cart(request,id):
    # return HttpResponse(id)
    if request.session.get('is_authenticated', True):
        Product = product.objects.get(productId = id)
        # chk = CartItems.objects.filter(game = game.gid)
        # if len(chk) > 0:
        #     is_added = True
        #     return redirect(reverse(indexPage),context = {'is_added':is_added}) 
        # else :
        User = request.session['username']
        user_id = user.objects.get(username = User)
        try:
            cart = Cart.objects.create( 
                UserId = user_id,
                completed = False
            )
            cartitem = CartItems.objects.create(cart = cart, product = Product)
        except Exception as e:
            return HttpResponse(e)
        return redirect("/shop")    
    else:
        return redirect("/login")

def cart(request):
    if request.session.get('is_authenticated', True):
        User = user.objects.get(username = request.session['username'])
        cart_data = Cart.objects.filter(UserId = User.UserId)
        cartIDs = []
        for data in cart_data:
            cartIDs.append(data.cart_id)
            # print(data.cart_id)
        
        cartItemsList = []
        for id in cartIDs:
            cart_items = CartItems.objects.filter(cart_id = id)
            # return HttpResponse(cart_items)
            for citem in cart_items:
                cartItemsList.append(citem.product_id)
        
        print(len(cartItemsList))
        ProductList = []
        for c_item_id in cartItemsList:
            Products = product.objects.filter(productId = c_item_id)
            for Product in Products:
                ProductList.append(Product)
        #print(ProductList)
        # return HttpResponse("hello")
        return render(request, 'cart.html', context={'Products': ProductList})
    else:
        return redirect("/login")

# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
#         cartitems = cart.cartitems_set.all()
#     else:
#         cartitems = []
#         cart = {"get_cart_total": 0, "get_itemtotal": 0}
#     return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})


# def checkout(request):
#     return render(request, 'checkout.html', {})

# def updateCart(request):
#     data = json.loads(request.body)
#     productId = data["productId"]
#     action = data["action"]
#     product = product.objects.get(id=productId)
#     customer = request.user.customer
#     cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
#     cartitem, created = CartItems.objects.get_or_create(cart = cart, product = product)

#     if action == "add":
#         cartitem.quantity += 1
#         cartitem.save()
#     return JsonResponse("Cart Updated", safe = False)


# def updateQuantity(request):
#     data = json.loads(request.body)
#     quantityFieldValue = data['qfv']
#     quantityFieldProduct = data['qfp']
#     product = CartItems.objects.filter(product__name = quantityFieldProduct).last()
#     product.quantity = quantityFieldValue
#     product.save()
#     return JsonResponse("Quantity updated", safe = False)