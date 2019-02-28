from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from application.models import Application

# Create your views here.

def index(request):
	num_apps = Application.objects.all().count()
	sci_apps = Application.objects.filter(faculty__contains='science').count()

	context = {
		'num_apps': num_apps,
		'sci_apps': sci_apps,
	}

	return render(request, 'index.html', context=context)
	# return HttpResponse("Hello, world. You're at the application index.")

class ApplicationListView(generic.ListView):
	model = Application
		
class ApplicationDetailView(generic.DetailView):
	model = Application