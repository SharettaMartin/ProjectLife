from django import forms
from .models import Donor, Patient, Response

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
          'name',
          'city',
          'blood_type',
          'donation_type'
        ]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
          'name',
          'city',
          'state',
          'blood_type',
          'need',
                  ]

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
          'message',
    ]

        