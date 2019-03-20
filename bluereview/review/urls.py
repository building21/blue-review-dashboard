from django.urls import path

from review import views

urlpatterns = [
	path('', views.index, name='review-index'),
	path('index/', views.ReviewListView.as_view(), name='review-list'),
	path('upload/', views.upload_reviews, name='review-upload'),
]
