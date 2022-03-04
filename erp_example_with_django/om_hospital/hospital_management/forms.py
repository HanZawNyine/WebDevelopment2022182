from .models import HospitalPatient
from django import forms


class NewPatientForm(forms.ModelForm):
    class Meta:
        model = HospitalPatient
        fields = ('name', 'age', 'gender', 'note', 'state')
