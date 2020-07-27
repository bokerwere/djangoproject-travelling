from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import  User ,auth

# Create your views here.
#create user account
def register(request):
    if  request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if password1==password2:
            #varify user
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
                #print("user name already taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
               user=User.objects.create_user(username=username,password=password1,email=email,last_name=last_name,first_name=first_name)
               user.save();
               print("user created")
               return  redirect('login')
        else:
            print("password not matching")
            messages.info(request,"password not matching")
            return redirect('register')

        return redirect('/')

    else:
       return render(request,'register.html')



#login
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")


    else:
        return render(request,'login.html')






def logout(reguest):
    auth.logout(reguest)
    return redirect('/')


