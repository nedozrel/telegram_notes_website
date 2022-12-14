from django.urls import path
from . import views

urlpatterns = [
	path('create-profile', views.create_profile, name='create-profile'),
	path('profile/<int:tg_user_id>/', views.get_profile, name='get-profile'),
	path('create-note', views.create_note, name='create-note'),
	path('notes/<int:creator_tg_id>/', views.get_notes, name='get-notes'),
	path('friends/<int:tg_user_id>/', views.get_user_friends, name='get-user-friends'),
]
