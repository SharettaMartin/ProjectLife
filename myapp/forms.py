from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
          'name',
          'city',
          'blood_type',
          'donation_type'
        ]
    