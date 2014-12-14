from django.conf.urls import patterns, url

from employees import views

urlpatterns = patterns('',
	#Grid view
    url(r'^$', views.index, name='index'),
	#Query view
	url(r'^query$', views.empquery, name='empquery'),
	#Query fields
	url(r'^fields$', views.empfields, name='empfields'),
)