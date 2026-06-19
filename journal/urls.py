from django.urls import path
from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('add/', views.add_reflection, name='add_reflection'),
    path('edit/<int:reflection_id>/', views.edit_reflection, name='edit_reflection'),
    path('delete/<int:reflection_id>/', views.delete_reflection, name='delete_reflection')
]
