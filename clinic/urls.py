from django.urls import path
from . import views

# Url to redirect
urlpatterns = [
    path('clinic/', views.clinic, name = 'clinic'),
    path('addpatient/', views.addpatient, name='addpatient'),
    path('addpatientdetails/', views.addpatientdetails, name='addpatientdetails'),
    path('addprescription/', views.addprescription, name='addprescription'),
    path('addforprescription/<str:pk>', views.addforprescription, name='addforprescription')
    
]