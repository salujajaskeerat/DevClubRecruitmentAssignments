from django.contrib.auth.models import User
	# this gives use base user class we can use 
from django import forms
from .models import Profile


class UserForm(forms.ModelForm):
	# this will create blueprint for our forms

	password=forms.CharField(widget=forms.PasswordInput())
	# this means hidden password
	class Meta:
		model=User
		fields=['username','email','password']
# class LoginForm(forms.ModelForm):
# 	password=forms.CharField(widget=forms.PasswordInput())
# 	class Meta :
# 		model=User
# 		fields=['username','password']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User 
		fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile 
		fields=['image']


