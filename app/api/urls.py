from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_notes),
    path('notes/<str:pk>/', views.get_note),
]