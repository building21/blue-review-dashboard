from django import forms

class ReviewUploadForm(forms.Form):
	csv = forms.FileField(label="Review csv File", allow_empty_file=False)
