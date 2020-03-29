from django.contrib.auth.models import User
	# this gives use base user class we can use 
from django import forms
from .models import *


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
	

	class Meta:
		model=User 
		fields=['username',]

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile 
		fields=['image']


class CommentForm(forms.ModelForm):
	class Meta:
		model=Comment
		fields=['content','anonymous',]

class ProfRatingForm(forms.ModelForm):
	class Meta:
		model=prof_review
		fields=['rating1',]

# class LikePost(forms.ModelForm):
# 	class Meta:
# 		model=Comment
# 		fields=['user','prof']