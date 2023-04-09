from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from auth_app.forms import UserRegistrationForm,SellerRegistrationForm, AdminRegistrationForm
from auth_app.models import user_registration,seller_registration, admin_registration
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth import authenticate, login


# Create your views here.
def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def merchant_login(request):
    return render(request,'merchant_login.html')

def merchant_registration(request):
    return render(request,'merchant_registration.html')

def admin_login(request):
    return render(request,'admin_login.html')
    
# def register(request):  
   
#     if request.method == "POST": 
        
#         form = UserRegistrationForm(request.POST or None)  
        
#         if form.is_valid():  
#             try:  
#                 form.save()  
#                 return HttpResponse(form)
#                 #return render(request,'login.html')  
#             except:  
#                 pass  
#     else:  
#         form = UserRegistrationForm()  
#     return render(request,'registration.html',{'form':form})

def register(request):  
    if request.method == "POST": 
        user_reg = user_registration()
        user_reg.username = request.POST.get('username')
        user_reg.email = request.POST.get('email')
        if user_registration.objects.filter(email=user_reg.email).exists():
            #raise ValidationError("Email Exits")
            return render(request,"registration.html") 
        user_reg.contact = request.POST.get('contact')
        user_reg.address = request.POST.get('address')
        user_reg.password = request.POST.get('password')

        subject = 'Welcome To E-Wish'
        message = f'Hello, {user_reg.username},Your registration has been confirmed for the E-Wish'
        email_from = settings.EMAIL_HOST_USER
        registration_list = [user_reg.username, user_reg.email]

        send_mail( subject, message, email_from, registration_list)

        if len(request.FILES) != 0:
            user_reg.image = request.FILES['image']
        
        user_reg.save()
        messages.success(request, "User registered successfully!")
        return render (request, "login.html")
    else:
        messages.error(request, "User registration failed!")
        return render (request, "registration.html")

def log(request):
    if request.method == "POST":    
        form = UserRegistrationForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        
        flag = 0
        data = user_registration.objects.all()
        
        obj = get_object_or_404(user_registration, username=un)
        result = check_password(ps, obj.password)
        
        if result == True:
            flag = 1
              
        # for i in range(len(data)):
        #     if data[i].username == un and data[i].password == ps:
        #             # request.session['username'] = data[i].username
        #             # request.session['email'] = data[i].email
        #             # request.session['phoneno'] = data[i].phoneno
                
        #             # username = request.session['username']
        #             # email = request.session['email']
        #             # phoneno = request.session['phoneno']
        #             # session_user = {'username': username, 'email': email, 'phoneno': phoneno, 'image_path': image_path}
        #         return render(request,'index.html')
        #         #return HttpResponse("Success")
        #     else :
        #         flag = 0
        if flag == 0:
            #return render(request,'login.html')
            return HttpResponse("Failed")
        else:
            return render(request,'index.html')
    
def seller_register(request):  
    if request.method == "POST": 
        seller_reg = seller_registration()
        seller_reg.username = request.POST.get('username')
        seller_reg.email = request.POST.get('email')
        if seller_registration.objects.filter(email=seller_reg.email).exists():
            #raise ValidationError("Email Exits")
            return render(request,"merchant_registration.html") 
        seller_reg.contact = request.POST.get('contact')
        seller_reg.companyname = request.POST.get('companyname')
        seller_reg.address = request.POST.get('address')
        seller_reg.password = request.POST.get('password')

        subject = 'Welcome To E-Wish'
        message = f'Hello, {seller_reg.username},Your registration has been confirmed for the E-Wish'
        email_from = settings.EMAIL_HOST_USER
        registration_list = [seller_reg.username, seller_reg.email]

        send_mail( subject, message, email_from, registration_list)

        if len(request.FILES) != 0:
            seller_reg.image = request.FILES['image']
        
        seller_reg.save()
        messages.success(request, "Seller registered successfully!")
        return render (request, "merchant_login.html")
    else:
        messages.error(request, "Seller registration failed!")
        return render (request, "merchant_registration.html")

def seller_log(request):
    if request.method == "POST":    
        form = SellerRegistrationForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        #ps = check_password(request.POST.get["password"])
        
        flag = 0
        data = seller_registration.objects.all()
        
        obj = get_object_or_404(seller_registration, username=un)
        result = check_password(ps, obj.password)
        
        if result == True:
            flag = 1
        
        # for i in range(len(data)):
        #     if data[i].username == un and data[i].password == ps:
        #             # request.session['username'] = data[i].username
        #             # request.session['email'] = data[i].email
        #             # request.session['phoneno'] = data[i].phoneno
                
        #             # username = request.session['username']
        #             # email = request.session['email']
        #             # phoneno = request.session['phoneno']
        #             # session_user = {'username': username, 'email': email, 'phoneno': phoneno, 'image_path': image_path}
        #         return render(request,'merchant_index.html')
        #         #return HttpResponse("Success")
        #     else :
        #         flag = 0
        if flag == 0:
            return render(request,'merchant_login.html')
            #return HttpResponse("Failed")
        else:
            return render(request,'merchant_index.html')


def admin_log(request):
    if request.method == "POST":    
        form = AdminRegistrationForm(request.POST)
        em = request.POST.get("email")
        ps = request.POST.get("password")
        #ps = check_password(request.POST.get["password"])
        
        flag = 0
        data = admin_registration.objects.all()
        for i in range(len(data)):
            if data[i].email == em and data[i].password == ps:
                    # request.session['username'] = data[i].username
                    # request.session['email'] = data[i].email
                    # request.session['phoneno'] = data[i].phoneno
                
                    # username = request.session['username']
                    # email = request.session['email']
                    # phoneno = request.session['phoneno']
                    # session_user = {'username': username, 'email': email, 'phoneno': phoneno, 'image_path': image_path}
                return render(request,'admin_index.html')
                #return HttpResponse("Success")
            else :
                flag = 0
        if flag == 0:
            return render(request,'admin_login.html')
            #return HttpResponse("Failed")

def admin(request):
    return render(request,'admin_index.html')
