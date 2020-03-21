from django.shortcuts import render

from django.views import generic
from .models import Proff

class IndexView (generic.ListView):
	template_name="review/index.html"
	context_object_name='Prof'
	def get_queryset(self): # this queries the database
		return Proff.objects.all()

class DetailView(generic.DetailView):
	model=Proff
	context_object_name='Prof'
	template_name="review/details.html"