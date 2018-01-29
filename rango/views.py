from django.shortcuts import render
from django.http import HttpResponse
""" Chapter 3 fix temporary
def index(request):
	#construct a dictionary to pass to the template engine as its context
	#note the key bold message is the same as {{boldmessage}} in the template!
	#context_dict = {'boldmessage': "Crunchy, Creamy, cookie, candy, cupcake!"}
	
	#Return a rendered response to send the client.
	# we make use of the shortcut function to make our lives easier.
	#
	
	return render(request, 'rango/index.html', context=context_dict)
"""
def index(request):
  	return HttpResponse("Rango says hey there partner!<br/> <a href='/rango/about/'>About</a>")
	
def about(request):
	return HttpResponse("Rango says here is the about page.<br/> <a href=\"/rango/\">Index</a>")