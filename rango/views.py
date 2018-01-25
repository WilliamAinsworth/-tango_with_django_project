from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#construct a dictionary to pass to the template engine as its context
	#note the key bold message is the same as {{boldmessage}} in the template!
	context_dict = {'boldmessage': "Crunchy, Creamy, cookie, candy, cupcake!"}
	
	#Return a rendered response to send the client.
	# we make use of the shortcut function to make our lives easier.
	#
	return render(request, 'rango/index.html', context=context_dict)
	
