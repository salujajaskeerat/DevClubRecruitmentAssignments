
from django.contrib.auth.decorators import login_required
# we will use this decorator to check if user is login before accesing the page  
from django.views import generic
from .models import Proff
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login 
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import UserForm ,LoginForm


class IndexView (generic.ListView):
	template_name="review/index.html"
	context_object_name='Prof'
	def get_queryset(self): # this queries the database
		return Proff.objects.all()

class DetailView(generic.DetailView):
	model=Proff
	context_object_name='Prof'
	template_name="review/details.html"

class UserFormView(View ):
	form_class=UserForm 
      	# This tells that the blueprint we made , we are gonna use it.
      	# make a page register.html to where we will render
	template_name="review/register.html"



	def get(self,request):
		form=self.form_class(None)
		return render(request,self.template_name,{'form':form})
      		# the above code does only display blank form to the user 
      		# the form blueprint is send as dictionary into register.html


      	# process the data
	def post(self,request):

		form=self.form_class(request.POST)


		if form.is_valid():

      			# we need to check if user entered correct form of data
			user=form.save(commit=False)
      			# this cretes a object of the form , but doesnot save it
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()



      			# now we need to return him to the login page we do

			user=authenticate(username=username,password=password)
      			


			if user is not None:
      				# this is just to vheck if user is not banned/disabled
				
				login(request,user)
      				# after user has logged in we have to redirect him to home
				return redirect('review:index')


		return render(request,(self.template_name),{'form':form})

@login_required
def profile(request):
	return render(request,'review/profile.html')