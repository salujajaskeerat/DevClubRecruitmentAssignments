from django.db import models

# Create your models here.
class Proff(models.Model):
	Name=models.CharField(max_length=100)
	email=models.CharField(max_length=40)
	Dpt=models.CharField(max_length=40)
	research=models.CharField(max_length=100)
	post=models.CharField(max_length=25)
