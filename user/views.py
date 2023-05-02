from django.shortcuts import get_object_or_404, redirect,render
from django.http import HttpResponse
from django.contrib import messages
from merchant.models import product
from auth_app.models import user
from user.models import Cart,CartItems, Bill, BillItems, Contact
from user.forms import ContactForm
from django.db.models import Q
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# import json
from django.contrib.auth.hashers import make_password , check_password


#from auth_app.forms import UserRegistrationForm  
#from auth_app.models import user_registration  

# Create your views here.
#@login_required(login_url='login')
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

def viewProduct(request,id):
    Product = product.objects.get(productId = id)
    return render(request,'viewProduct.html',{'Product':Product})

#def back(request):
    #return render(request,'shop.html')

def profile(request):
    if request.session.get('is_authenticated', True):
        return render(request,'profile.html')
    else:
        return redirect("/login")

def gallery(request):
    obj = product.objects.filter(isApproved = True)
    return render(request,'gallery.html',{'image' : obj})

# def my_account(request):
#     return render(request,'my_account.html')

# def shop_detail(request):
#     return render(request,'shop_detail.html')

from django.db.models import Q

def shop(request):
    query = request.GET.get('query')
    if query:
        obj = product.objects.filter(Q(categoryName__categoryName__icontains=query) | 
                                     Q(subcategoryName__subcategoryName__icontains=query) |
                                     Q(dietType__dietType__icontains=query) | 
                                     Q(productName__icontains=query),
                                     isApproved=True)
    else:
        obj = product.objects.filter(isApproved=True)
    
    for prod in obj:
        ratings = prod.ratings_set.all().aggregate(Avg('productRating'))
        prod.average_rating = ratings['productRating__avg']
        
    if not obj.exists():
        messages.warning(request, 'No results found.')
        return redirect('/shop')
        
    return render(request, 'shop.html', {'product': obj})


def userlogout(request):
    try:
        del request.session['username'] 
        del request.session['email'] 
        del request.session['contact'] 
        del request.session['userAddress'] 
        del request.session['id'] 
        del request.session['city'] 
        del request.session['state'] 
        return render(request,'login.html')
    except Exception as e:
        return HttpResponse(e)
    return render(request,'login.html')

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

def remove_cart(request, id):
    if request.session.get('is_authenticated', True):
        cartitem = CartItems.objects.get(product_id=id)
        cart_id = cartitem.cart_id
        cartitem.delete()
        # Delete the cart if it has no cart items left
        cart_items = CartItems.objects.filter(cart_id=cart_id).count()
        if cart_items == 0:
            Cart.objects.filter(cart_id=cart_id).delete()
            return redirect("/cart")
        else:
            return redirect('/login')
  
# def remove_cart(request,id):
#     # return HttpResponse(id)
#     if request.session.get('is_authenticated', True):
#         # obj1 = get_object_or_404(product, ProductId = id)
#         cartitem = CartItems.objects.get(product_id = id)
        
        
#         # cart = get_object_or_404(Cart, cart_id = )
        
#     if request.method == "GET":
#         cartitem.delete()
#         return redirect("/cart")    
    # else:
    #     return redirect("/login")

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
    
def changePassword(request):
    return render(request,'changePassword.html')

def user_change_password(request):
    if request.method == "POST":    
        old_pswd = request.POST.get("password")
        username1 = request.POST.get("username1")
    
        obj = get_object_or_404(user, username = username1)
        
        result = check_password(old_pswd, obj.password)
        if obj.user_type == 1 and result == True:
            new_pswd = request.POST.get("new_password")
            cnfm_pswd = request.POST.get("cnfm_password")
            
            if new_pswd == cnfm_pswd:
                
                obj.password = make_password(new_pswd)
                obj.save()
                
                messages.success(request, "Password Changed successfully!")
                return render(request,'changePassword.html')
            else :
                messages.error(request, "New Password and Confirm Password doesn't match!")
                return render(request, 'changePassword.html')
        else:
            messages.error(request, "Old is password is not correct!")
            return render(request, 'changePassword.html')

def buy_now(request):
    user_id = request.session['id']
    cart_items = CartItems.objects.filter(cart__UserId=user_id)
    
    if request.method == 'POST':
        totalPrice = request.POST.get("total")
        bill = Bill.objects.create(UserId_id=user_id, total_price=totalPrice)

    total_Items_In_Cart = request.POST.get('total_Items_In_Cart') 

    data = {}
    
    for counter in range(1, int(total_Items_In_Cart)+1):
        data[counter] = {
            # "product_key":request.POST.get(f'prod_{counter}'),
            # "points":request.POST.get(f'points_{counter}'),
            "qty": request.POST.get(f'quantity_{counter}')
        }
        print(f'quantity_{counter}')
        print(request.POST.get(f'quantity_{counter}'))
    counter = 1
    for item in cart_items:
        # quantity = request.POST.get("quantity")
        BillItems.objects.create(Bill_id=bill, cart=item.cart, productId = item.product, productQty = data[counter]['qty'])
        counter += 1
        item.cart.completed = True
        item.cart.save()
        item.delete()

    return redirect('/shop')

def feedback(request):  
    if request.method == "POST": 
        c_form = ContactForm(request.POST or None)
        # return HttpResponse(c_form) 
        if c_form.is_valid():
            c_form.save()
            messages.success(request, "Feedback send successfully!")
            #context = { 'subcategory_data': Sub_Categories.objects.all()}
            return render(request,'contact.html')
        
        else:
            messages.error(request, "Failed to send feedback")
            return render(request,'contact.html')
    else:
        messages.error(request, "Fill the form correctly!")
        return render(request,'contact.html')
    
# view bill history
def billHistory(request):
    # return HttpResponse('success')
    context = {}
    user_id = request.session['id']
    data = Bill.objects.filter(UserId_id = user_id)
    
    return render(request,"billHistory.html", context={'data':data})

def billDetails(request,id):
    # return HttpResponse(id)
    context = {}
    # user_id = request.session['id']
    data = BillItems.objects.filter(Bill_id_id = id)
    
    return render(request,"billDetails.html", context={'data':data, 'id':id})

# def search(request):
#     query = request.GET.get('q')
#     results = []
#     if query:
#         results = product.objects.filter(Q(productName__icontains=query) | Q(productDesc__icontains=query))
#     return render(request, 'search.html', {'query': query, 'results': results})
