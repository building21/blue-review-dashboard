import csv
import codecs
from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models

from application.models import Application
from review.models import Review

def handle_review_csv(csv_file, user_who_uploaded):
	csv_file_text_mode = codecs.iterdecode(csv_file, "utf-8")
	csv_reader = csv.reader(csv_file_text_mode, delimiter=',')
	for row in csv_reader:
		try:
			first_email = row[0]
			second_email = row[1]
			first_application = Application.objects.filter(email=first_email).first()
			second_application = Application.objects.filter(email=second_email).first()
			winner = True if row[2] == "1" else False
			user = user_who_uploaded
			time = datetime.now()
			in_prog = False
			completed = True
			review = Review(winner=winner, 
					user=user, 
					time=time, 
					in_prog=in_prog, 
					completed=completed)
			review.apps.add(first_application, second_application)
			review.full_clean()
		except ValidationError as e:
			"""Fields are not valid."""
			return True, "The csv fields are not valid."
		else:
			review.save()
	return False, "Uploaded reviews"
