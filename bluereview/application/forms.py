from django import forms

class ApplicationUploadForm(forms.Form):
    csv = forms.FileField(label="Application csv File", allow_empty_file=False)

