# Define url pattern for learning_logs

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
	# Home page
	path('', views.index, name = 'index')

	# Show all topics
	path('topics', views.topic, name = 'topics')
]