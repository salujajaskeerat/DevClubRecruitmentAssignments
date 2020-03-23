from django.db import models
# now let us add feature to add profile pic of our users
from django.contrib.auth.models import User

# Create your models here.
class department(models.Model):
	dept_name=models.CharField(max_length=30)
	def __str__(self):
		return self.dept_name
class Proff(models.Model):
	department=models.ForeignKey(department,on_delete=models.CASCADE,null=True)
	Name=models.CharField(max_length=100)
	email=models.CharField(max_length=40)
	Dpt=models.CharField(max_length=40)
	research=models.CharField(max_length=100)
	post=models.CharField(max_length=25)
	image=models.FileField()

	def __str__(self):
		return self.Name



class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	# we are basically using username as the primary key for our project
	image=models.FileField(default='default.png')

	def __str__(self):
		return f'{self.user.username} Profile'


class Comment(models.Model):
	prof=models.ForeignKey(Proff ,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	content=models.TextField(max_length=300)

	timestamp=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return '{}.{}'.format(self.prof.Name,str(self.user.username))