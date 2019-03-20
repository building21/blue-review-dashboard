from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from application.models import Application
from application.helper import handle_application_csv
from application.forms import ApplicationUploadForm

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
	if request.method == 'POST':
		form = ApplicationUploadForm(request.POST, request.FILES)
		if form.is_valid():
			error, confirmation = handle_application_csv(form.cleaned_data['csv'])
		else:
			error = True
	else:
		form = ApplicationUploadForm
		confirmation = None
		error = False

	context = {
		'form': form,
		'error': error,
		'confirmation': confirmation
	}

	return render(request, 'upload.html', context=context)

class ApplicationListView(LoginRequiredMixin, generic.ListView):
	model = Application
		
class ApplicationDetailView(LoginRequiredMixin, generic.DetailView):
	model = Application
