from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from review.models import Review
from review.helper import handle_review_csv
from review.forms import ReviewUploadForm

# Create your views here.

def index(request):
	# return render(request, 'index.html')
	return HttpResponse("Hello, world. You're at the reviews index.")

@permission_required('review.can_upload')
def upload_reviews(request):
	if request.method == 'POST':
		form = ReviewUploadForm(request.POST, request.FILES)
		if form.is_valid():
			error, confirmation = handle_review_csv(form.cleaned_data['csv'])
		else:
			error = True
	else:
		form = ReviewUploadForm 
		confirmation = None
		error = False

	context = {
		'form': form,
		'error': error,
		'confirmation': confirmation
	}

	return render(request, 'upload.html', context=context)

class ReviewListView(PermissionRequiredMixin, generic.ListView):
	model = Review
	permission_required = ('review.can_view_list')