from django.contrib import admin
from django.urls import path
from . views import patient_list,patient_create

app_name="HospitalManagement"

urlpatterns = [
    path('', patient_list,name="patient_list"),
    path('patient_list&type=list', patient_list,name="patient_list_List"),
    path('patient_list&type=kanban', patient_list,name="patient_list_kanban"),
    path('patient_create/', patient_create,name="patient_create"),
]
