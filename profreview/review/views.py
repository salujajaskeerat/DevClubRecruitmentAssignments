
from django.contrib.auth.decorators import login_required
# we will use this decorator to check if user is login before accesing the page  
from django.views import generic
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate , login 
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import *
from django.contrib import messages
from . import functions
class IndexView (generic.ListView):
	template_name="review/index.html"
	context_object_name='dept'
	def get_queryset(self): # this queries the database
		return department.objects.all()


#lets make a index view for the each of department's professor
def prof_index(request,pk):
	template_name="review/proflist.html"
	Prof =Proff.objects.filter(department=pk)
	return render(request,template_name,{'Prof':Prof})
# this is prof details view , which we can acess

def prof_details(request,pk):
	template_name="review/details.html"
	prof=Proff.objects.filter(pk=pk)
	Prof=prof[0]

	comment=Comment.objects.filter(prof=pk).order_by('id')
		# this store all ratings for this prof
	r=prof_review.objects.filter(prof=Prof)
	#Lets calculate his Previous Ratings
	net_rating=functions.net_rating(r)
	total_ratings=r.count()
	user_rating=None
	if request.user.is_authenticated:
		# it means that user is logged in 
		if(prof_review.objects.filter(prof=Prof,user=request.user).exists()):
			user_rating=prof_review.objects.get(prof=Prof,user=request.user).rating1
		
	
		
	if request.method=='POST':
		comment_form=CommentForm(request.POST)
		if(comment_form.is_valid):
			content=request.POST.get('content')
			c=Comment.objects.create(prof=Prof,user=request.user,content=content)
			c.save()
			return redirect('review:details')
	else:
		comment_form=CommentForm()
	# this gives us the requires proff on the list

		context={
	'Prof':Prof,
	'comment':comment,
	'comment_form':comment_form,
	'net_rating':net_rating,
	'total_ratings':total_ratings,
	'user_rating':user_rating,
	}

	return render(request,template_name,context)

#

# we used this before
# class DetailView(generic.DetailView):
# 	model=Proff
# 	context_object_name='Prof'
# 	template_name="review/details.html"

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
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,
			request.FILES,
			instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'your account has been Updated')
			return redirect('review:profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm(instance=request.user.profile)
	# we have created empty user and profile update form
	# Now we will pass these forms into our template
	context={
		'u_form':u_form,
		'p_form':p_form,
	}
	return render(request,'review/profile.html',context)

@login_required
def prof_rating(request,pk):
	template_name='review/prof_rating.html'
	Prof=Proff.objects.get(pk=pk)

	# this store all ratings for this prof
	r=prof_review.objects.filter(prof=Prof)
	#Lets calculate his Previous Ratings
	net_rating=functions.net_rating(r)
	total_ratings=r.count()
	
	
		# Here we will pass form to user To allow him to Rate


	

	if request.method=='GET':

		r_form=ProfRatingForm()
		context={
		'Prof':Prof,
		'net_rating':net_rating,
		'total_ratings':total_ratings,
		'r_form':r_form,
		}
		return render(request,template_name,context)

	else:
		r_form=ProfRatingForm(request.POST)
		if(r_form.is_valid()):
			rating1=request.POST.get('rating1')
			r=prof_review.objects.create(prof=Prof,user=request.user,rating1=rating1)
			r.save()
			
			return redirect('review:details',pk)
		context={
		'Prof':Prof,
		'net_rating':net_rating,
		'total_ratings':total_ratings,
		'r_form':r_form,
		}
		context={'Prof':Prof,'net_rating':net_rating,'total_ratings':total_ratings}
		return render(request,template_name,context)

