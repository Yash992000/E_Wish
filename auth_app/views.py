from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
# from auth_app.forms import UserRegistrationForm,SellerRegistrationForm, AdminRegistrationForm
# from auth_app.models import user_registration,seller_registration, admin_registration

from auth_app.forms import BasicReg
from auth_app.models import user,merchant, customer
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    return render(request,'login.html')

def Cregistration(request):
    return render(request,'CustRegistration.html', {'type':1})

def merchant_registration(request):
    return render(request,'merchant_registration.html', {'type':2})

def admin_login(request):
    return render(request,'admin_index.html')

def register(request):  
    if request.method == "POST": 
        user_reg = user()
        user_reg.username = request.POST.get('username')
        user_reg.email = request.POST.get('email')
        if user.objects.filter(email=user_reg.email).exists():
            #raise ValidationError("Email Exits")
            return render(request,"CustRegistration.html") 
        user_reg.contact = request.POST.get('contact')
        add = request.POST.get('userAddress')
        user_reg.password = request.POST.get('password')
        user_reg.user_type = request.POST.get('user_type')
        utype = int(request.POST.get('user_type'))
        user_reg.password = make_password(user_reg.password)

        if len(request.FILES) != 0:
            user_reg.image = request.FILES['image']
        user_reg.save()
        # user_reg.image = request.POST.get('image')

        # subject = 'Welcome To E-Wish'
        # message = f'Hello, {user_reg.username},Your registration has been confirmed for the E-Wish'
        # email_from = settings.EMAIL_HOST_USER
        # registration_list = [user_reg.username, user_reg.email]
        # send_mail(subject, message, email_from, registration_list)

        # return HttpResponse(user_reg.user_type)
        
        if utype == 1:
            if request.method == "POST": 
                customer_reg = customer()
                customer_reg.userAddress = request.POST.get('userAddress')
                customer_reg.UserId = user_reg           
                
                subject = 'Welcome To E-Wish'
                message = f'Hello, {user_reg.username},Your registration has been confirmed for the E-Wish'
                email_from = settings.EMAIL_HOST_USER
                registration_list = [user_reg.username, user_reg.email]

                send_mail(subject, message, email_from, registration_list)
                
                customer_reg.save()
                messages.success(request, "User registered successfully!")
                return render (request, "login.html")
            else:
                messages.error(request, "User registration failed!")
                return render (request, "CustRegistration.html")
        
        elif utype == 2:
            if request.method == "POST": 
                merch_reg = merchant()
                merch_reg.shopPhone = request.POST.get('shopPhone')
                merch_reg.shopName = request.POST.get('shopName')
                merch_reg.shopAddr = request.POST.get('shopAddr')
                merch_reg.UserId = user_reg              
                
                subject = 'Welcome To E-Wish'
                message = f'Hello, {user_reg.username},Your registration has been confirmed for the E-Wish'
                email_from = settings.EMAIL_HOST_USER
                registration_list = [user_reg.username, user_reg.email]

                send_mail(subject, message, email_from, registration_list)
                
                merch_reg.save()
                messages.success(request, "Merchant registered successfully!")
                return render (request, "login.html")
            else:
                messages.error(request, "Merchant registration failed!")
                return render (request, "CustRegistration.html")
    else:
        #messages.error(request, "User registration failed!")
        return render(request, "CustRegistration.html")

    return render(request, "CustRegistration.html")

def log(request):
    if request.method == "POST":    
        form = BasicReg(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        
        obj = get_object_or_404(user, username=un)
        utype = obj.user_type
        # return HttpResponse(utype)    
        result = check_password(ps, obj.password)
        #return HttpResponse(result)
        admin = obj.isAdmin
      
        if admin == 1 and result == True:
            return render(request, 'admin_index.html')        

        if result == True:
            if utype == 1:
                data = user.objects.get(username = un)
                custo = customer.objects.get(UserId = data.UserId)
                
                request.session['username'] = data.username
                request.session['id'] = data.UserId
                request.session['email'] = data.email
                request.session['contact'] = data.contact
                request.session['userAddress'] = custo.userAddress
                request.session['is_authenticated'] = True
                return render(request,'index.html')
            
            elif utype == 2:
                data = user.objects.get(username = un)
                print(data)
                merch = merchant.objects.get(UserId = data.UserId)    
                request.session['username'] = data.username
                request.session['id'] = data.UserId
                request.session['email'] = data.email
                request.session['contact'] = data.contact
                request.session['shopName'] = merch.shopName
                request.session['shopAddr'] = merch.shopAddr
                request.session['shopPhone'] = merch.shopPhone
                request.session['is_authenticated'] = True
                return render(request,'merchant_index.html')                    
        else:
            messages.error(request, "User login failed!")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def admin(request):
    return render(request,'admin_index.html')