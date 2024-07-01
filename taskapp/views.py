from django.shortcuts import render , redirect
from .forms import userform
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from .models import signup
from django.contrib.auth.models import User
from django.contrib.auth import login,logout ,authenticate ,get_user_model
import time
# Create your views here.
def index(request):
    return render(request,'index.html')



def patientlogin(request):
    
    pt = userform(request.POST)
    if request.method == 'POST': 
        if pt.is_valid():
            username = pt.cleaned_data['username']
            password = pt.cleaned_data['password']
            newuser = authenticate(username = username , password = password)
           
            
            
            if newuser is not None and newuser.is_patient == True: 
                login(request,newuser)
         
                return redirect('patientdashboard')
            else:
                messages.error(request,"Invalid Username and Password")
                
        else:
            print('Not Valid form')

    return render(request,'patientlogin.html',{'form': pt})

def doctorlogin(request):
    dt = userform(request.POST)
    if request.method == 'POST': 
        if dt.is_valid():
            username  = dt.cleaned_data['username']
            password = dt.cleaned_data['password']
            user = authenticate(username = username , password = password)
        
            if user is not None and user.is_doctor == True: 
                login(request,user)
           
                return redirect('doctordashboard')
            else:
                messages.error(request,"Invalid Username and Password")
                
        else:
            print('Not Valid form')
    
    return render(request,'doctorlogin.html',{'form': dt})


def patientsignup(request):
    if request.method == 'POST' :
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        profile_picture  = request.FILES.get('profile_picture')
        username  = request.POST.get('username')

        email  = request.POST.get('email')
        password  = request.POST.get('password')
        confirm_password  = request.POST.get('confirm_password')
        address_line1  = request.POST.get('address_line1')

        city  = request.POST.get('city')
        state  = request.POST.get('state')
        pincode  = request.POST.get('pincode')
        User = get_user_model()
       
        
        if password == confirm_password:
            
            my_user = User.objects.create_user(username = username , email = email ,password = password)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.email = email
            my_user.username = username
            my_user.is_patient = True
            my_user.save()
            
            user = signup(first_name = first_name , last_name = last_name , profile_picture = profile_picture , username = username , email = email,
                      password = password , address_line1 = address_line1 , city = city , state =state, 
                      pincode = pincode ) 
            user.is_patient = True 
            
            user.save() 
           
            
            messages.success(request,'Signup Successfull')
            
            return redirect("patientlogin")
            
        else:
            messages.error(request,'password and confirmPassword Not matched')
            
            
        

    return render(request , 'patientsignup.html')                                                                                   

def doctorsignup(request):
    if request.method == 'POST' :
        first_name  = request.POST.get('first_name')
        last_name  = request.POST.get('last_name')
        profile_picture  = request.FILES.get('profile_picture')
        username  = request.POST.get('username')

        email  = request.POST.get('email')
        password  = request.POST.get('password')
        confirm_password  = request.POST.get('confirm_password')
        address_line1  = request.POST.get('address_line1')

        city  = request.POST.get('city')
        state  = request.POST.get('state')
        pincode  = request.POST.get('pincode')
        User = get_user_model()
        
       
           
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('patientsignup')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already used")
                return redirect('patientsignup')
            
            user = signup(first_name = first_name , last_name = last_name , profile_picture = profile_picture , username = username , email = email,
                      password = password , address_line1 = address_line1 , city = city , state =state, 
                      pincode = pincode  ) 
            user.save() 
            
            my_user = User.objects.create_user(username = username , email = email ,password = password)
            my_user.first_name = first_name
            my_user.last_name = last_name
            my_user.email = email
            my_user.is_doctor = True 
            my_user.save()
        
            
           
           
           
            messages.success(request,'Signup Successfull')
            
            return redirect("doctorlogin")
            
        else:
            messages.error(request,'password and confirmPassword Not matched')
    return render(request , 'doctorsignup.html')
    


def patientdashboard(request):
    user = request.user
    
    return render(request , 'patientdashboard.html' ,{'User' : user})



def doctordashboard(request):
    user = request.user
    return render(request , 'doctordashboard.html',{'User' : user})


def logoutuser(request):
    logout(request)
    messages.success(request,' logout successfully')
    
    return redirect('index')