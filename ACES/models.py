from django.db import models

# Create your models here.
#this model is not used in this webpage at all!
class User(models.Model):
	user=models.CharField(max_length=100)
	email=models.CharField(max_length=400)
	password=models.CharField(max_length=100)


	def __str__(self):
		return self.user