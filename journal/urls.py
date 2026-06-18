from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('add/', views.add_reflection, name='add_reflection'),
]
