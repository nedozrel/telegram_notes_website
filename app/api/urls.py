from django.urls import path
from . import views

urlpatterns = [
	path('create-profile', views.create_profile, name='create-profile'),
	path('notes/<int:creator_tg_id>/', views.get_notes, name='get-note'),
	path('create-note', views.create_note, name='create-note'),
]
