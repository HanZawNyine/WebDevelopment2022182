from django.shortcuts import render
from .models import HospitalPatient
from .forms import NewPatientForm

# Create your views here.
def patient_list(request):
    patients = HospitalPatient.objects.all()
    # if request.path != "/patient_list&type=kanban":
    return render(request, 'hospital_management/patient/patient_list.html', {"patients": patients})
    # else:
    #     print("aa")
    # return render(request, 'hospital_management/patient/patient_list_kanban.html', {"patients": patients})


def patient_create(request):
    new_patient = NewPatientForm()
    return render(request, 'hospital_management/patient/patient_create.html',{'new_patient':new_patient})
