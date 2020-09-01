from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from  django.contrib  import  messages
#import form
from .forms import  UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#decorators add functiolities to the existing function
from django.contrib.auth.decorators import  login_required

# Create your views here.
def register(request):
    if request.method=="POST":

         #create instance of form
      form=UserRegisterForm(request.POST)
      if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request, f' you account have been created  {username}! . You are able to login')
             print("hellloooooooooooo")
             return redirect('login')
    else:
        form =UserRegisterForm()


    return render(request, 'register.html', {'form':form})

    #return HttpResponse('welocome')
#login_required  decorate enable user to login fast before accessing the profile.
@login_required
def profile(request):
    if request.method=='POST':

         u_form=UserUpdateForm(request.POST, instance=request.user)
         p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
         if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request, f' you account have been created !!')
             return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)




    context={ 'u_form':u_form, 'p_form':p_form }
    return render(request, "profile.html", context)
