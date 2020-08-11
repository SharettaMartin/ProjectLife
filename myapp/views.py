# from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DonorForm, PatientForm, ResponseForm
from .models import Donor, Patient


# Create your views here.POST]

def home(request):
   return render(request, 'myapp/landing.html', {})

def patient(request):
  form = PatientForm()
  if request.method == 'POST':
    form = PatientForm(request.POST)
    if form.is_valid():
     
      patient = form.save(commit=False)
      patient.user = request.user
      patient.save()
      return redirect(to='patient_dashboard', pk=patient.pk)
  context = {
    'form': form
  }
  return render(request, 'myapp/patient.html', context)

def profile(request, pk):
  patient = get_object_or_404(Patient, pk=pk)
  return render(request, 'myapp/public_profile.html', {"patient": patient})

def patient_detail(request, pk):
  patient = get_object_or_404(Patient, pk=pk)
  form = ResponseForm()
  if request.method == 'POST':
    form = ResponseForm(request.POST)
    if form.is_valid():
      response = form.save(commit=False)
      response.patient = patient
      response.save()
      return redirect(to='instructions')
  context = {
    'form': form
  }
  return render(request, 'myapp/detail.html', context)

@login_required
def new_donor(request):
    
    form = DonorForm(request.POST or None)
    
    if form.is_valid():
        donor = form.save(commit=False)
        donor.user = request.user
        donor.save()
        return redirect(to='home')
    context = { 
        'form': form
     }
    return render(request, 'myapp/donor_create.html', context)

def instructions(request):
   return render(request, 'myapp/instructions.html', {})
# def home(TemplateView):
    # template = 'home/home.html'

   # def get(self, request):
    #  form = PatientForm() (request.POST)
     # return render(request, self.template_name, {'form':form})
     # text = form.cleaned_data ['post']
     # form = PatientForm
     # return redirect ('home:home')

     # args = {"form".form} ('text'.text)
     # return render(request, self.template_name, args)

  
    # def post(self.request):
    
# def donor(request):
#     if request.method == 'GET':
#           form = ContactForm()
#     else:
#           form = ContactForm(data=request.POST)
#           if form.is_valid():
#               form.save()
#               return redirect(to='')
#       return render(request, 'myapp/donor.html', {})

# def list_contacts(request):
#     contacts = Contact.objects.all()
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_contacts')
#     return render(request, "contacts/list_contacts.html",
#                   {"contacts": contacts, 'form':form})


# def add_contact(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_contacts')

#     return render(request, "contacts/add_contact.html", {"form": form})

  