from django.urls import path
from . import views

urlpatterns = [
	path('create-profile', views.create_profile, name='create-profile'),
	path('notes/', views.get_notes, name='get-notes'),
	path('notes/<str:pk>/', views.get_note, name='get-note'),
	path('create-note', views.create_note, name='create-note'),
]
