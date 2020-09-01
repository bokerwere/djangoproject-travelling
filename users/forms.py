from  django import forms
from django.forms import ModelForm
from  django.contrib.auth.models import User
from  django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    #adding fields
    email=forms.EmailField()
    #meta clsas give namespace for nesting  and configuration
    class Meta:
        model=User
        #fields to be display
        fields=['username','email','password1','password2']



class UserUpdateForm(forms.ModelForm):
    #adding fields
    email=forms.EmailField()
    #meta clsas give namespace for nesting  and configuration
    class Meta:
         model=User
         #fields to be display
         fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
         model=Profile
         fields=['image']