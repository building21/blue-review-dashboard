from django.contrib import admin

# Register your models here.

from review.models import Review

# admin.site.register(Review)

# Define custom admin class
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_filter = ('in_prog', 'completed', 'user')