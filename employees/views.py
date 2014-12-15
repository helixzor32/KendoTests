import json
from django.db.models import Q
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

	#Pull request 
	reqs = request.GET

	#Handle sorting/filtering (if any)
	filterop = ''
	filterfield = ''
	sortdir = ''
	sortfield = ''
	
	#Pull all data
	e = employees.objects.all()

	#Sorts
	if reqs.__contains__('sort[0][dir]'):
		#Pull involved field
		sortdir = reqs.get('sort[0][dir]')
		sortfield = reqs.get('sort[0][field]')
	
		#Set up request (with descending sign if needed)
		ordsign = ''
		if sortdir == 'desc':
			ordsign = '-'
		sortfield = ordsign + sortfield
		
		#Apply sort
		e = e.order_by(sortfield)
	
	#Filtering (determine off 0 index option)
	if reqs.__contains__('filter[filters][0][field]'):
		#There is filtering - let's read them all (tricky...)
		x = 0
		Qr = None
		while(x >= 0):
			#Set compare index
			ind = str(x)
			
			#Does this index exist?
			filterop = reqs.get('filter[filters][' + ind + '][operator]')
			
			#Anything found for this index?
			if not filterop:
				break
				
			#Continue
			filterfield = reqs.get('filter[filters][' + ind + '][field]')
			filterval = reqs.get('filter[filters][' + ind + '][value]')
			
			#Based off the operator - set up the appropriate filter
			if filterop == "startswith":
				q = Q(**{"%s__startswith" % filterfield: filterval })
			elif filterop == "eq":
				q = Q(**{"%s__iexact" % filterfield: filterval })
			elif filterop == "con":
				q = Q(**{"%s__contains" % filterfield: filterval })

			if Qr:
				Qr = Qr & q
			else:
				Qr = q
				
			#Increment pointer
			x = x + 1
				
		#Now issue call	(with all filters set)
		e = e.filter(Qr)
		
	#Read through remaining fields and set up return list
	for fields in e:		
		#Set up entry
		record = {'id' : fields.id, 'fname' : fields.fname, 'lname' : fields.lname, 'city' : fields.city, 'title' : fields.title, 'dob' : str(fields.dob), 'age' : fields.age }
		emp_records.append(record)
		
	#Return results
	return HttpResponse(json.dumps(emp_records), content_type="application/json")

#View handling for columns on grid
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

#View handling for city dropdown
def empcities(request):
	cities = []
	
	list = employees.objects.values('city').distinct('city')
	for city in list:
		cities.append(city)
	final = {}
	final['d'] = cities
	return HttpResponse(json.dumps(final), content_type="application/json")