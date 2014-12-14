from django.db import models

#Employee model
class employees(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	dob = models.DateTimeField('date of birth')
	age = models.IntegerField()