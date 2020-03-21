from django.contrib.auth.models import User
	# this gives use base user class we can use 
from django import forms


class UserForm(forms.ModelForm):
	# this will create blueprint for our forms

	password=forms.CharField(widget=forms.PasswordInput())
	# this means hidden password
	class Meta:
		model=User
		fields=['username','email','password']
class LoginForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta :
		model=User
		fields=['email','password']