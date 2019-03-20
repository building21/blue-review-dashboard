from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Review(models.Model):
	# Fields
	apps = models.ManyToManyField('application.Application')
	# app_b = models.ForeignKey('application.Application', on_delete=models.PROTECT)
	winner = models.BooleanField(blank=True)
	user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, blank=True, null=True)
	time = models.DateTimeField(blank=True, null=True)
	in_prog = models.BooleanField(blank=True)
	completed = models.BooleanField(blank=True)

	# Metadata
	class Meta(object):
		ordering = ['id']
		permissions = (
			('can_upload', "Can upload reviews to the database"),
			('can_review', "Can submit review decisions"),
			('can_view_list', "Can view list of reviews"),
			)

	# Functions
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of the model."""
		return reverse('model-detail-view', args=[str(self.id)])

	def __str__(self):
		return "<Review: %s vs %s>" % (self.winner, self.loser)
