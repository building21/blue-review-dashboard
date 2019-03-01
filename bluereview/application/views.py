from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from application.models import Application

# Create your views here.

@login_required
def index(request):
	num_apps = Application.objects.all().count()
	sci_apps = Application.objects.filter(faculty__contains='science').count()

	context = {
		'num_apps': num_apps,
		'sci_apps': sci_apps,
	}

	return render(request, 'index.html', context=context)
	# return HttpResponse("Hello, world. You're at the application index.")

@permission_required('application.can_upload')
def upload_applications(request):
	return render(request, 'index.html')

class ApplicationListView(LoginRequiredMixin, generic.ListView):
	model = Application
		
class ApplicationDetailView(LoginRequiredMixin, generic.DetailView):
	model = Application