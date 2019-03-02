from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from review.models import Review
from review.helper import handle_review_csv
from review.forms import ReviewUpoadForm

# Create your views here.

def index(request):
	# return render(request, 'index.html')
	return HttpResponse("Hello, world. You're at the reviews index.")

@permission_required('review.can_upload')
def upload_reviews(request):
	if request.method == 'POST':
		form = ReviewUpoadForm(request.POST)
		if form.is_valid():
			confirmation = handle_review_csv(form.cleaned_data['csv'])
		else:
			confirmation = "Error in your form"
	else:
		form = ReviewUpoadForm 
		confirmation = None

	context = {
		'form': form,
		'confirmation': confirmation
	}

	return render(request, 'upload.html', {'form': form})

class ReviewListView(PermissionRequiredMixin, generic.ListView):
	model = Review
	permission_required = ('review.can_view_list')