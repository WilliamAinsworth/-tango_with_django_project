from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category
from rango.models import Page

def index(request):
	#query for aall categories, order by likes, return top 5
	category_list= Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]

	context_dict = {'categories': category_list, 'pages': page_list}
	
	#Return a rendered response to send the client.
	return render(request, 'rango/index.html', context_dict)
	
def about(request):
	return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
	#dict for rendering engine
	context_dict={}

	try:
		#returns one model or raises exception
		category = Category.objects.get(slug=category_name_slug)

		#gets all associated pages, list of pages
		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages
		context_dict['category'] = category

	except Category.DoesNotExist:
		#category doesn't exit
		#do nothing

		context_dict['category'] = None
		context_dict['pages'] = None

	return render(request, 'rango/category.html', context_dict)
