import json
import pprint
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.db import models
from employees.models import employees
from django.core import serializers

# Create your views here.
def index(request):
	return render(request, 'empgrid.html')

def empquery(request):
	#Initialize response
	emp_dict = {}
	emp_records = []
	
	#Get data
	id = 1
	e = employees.objects.all()
	for fields in e:		
		#Set up entry
		record = {'id' : id, 'fname' : fields.fname, 'lname' : fields.lname, 'city' : fields.city, 'title' : fields.title, 'dob' : str(fields.dob), 'age' : fields.age }
		emp_records.append(record)
	
	#Set in results
	emp_dict['results'] = emp_records
	return HttpResponse(json.dumps(emp_dict), content_type="application/json")
	
def empfields(request):
	#Initialize response
	fieldList = {}
	
	#Get fields
	i = 1
	x = employees._meta.fields
	for field in x:
		type = field.get_internal_type()
		name = field.name
		fieldList[i] = {'name' : name, 'type' : type}
		i = i + 1
		
	#Get data
	#e = employees.objects.all()
	return HttpResponse(json.dumps([fieldList]), content_type="application/json")
