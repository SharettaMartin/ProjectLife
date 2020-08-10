# from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import DonorForm
from .models import Donor, Patient


# Create your views here.POST]

def home(request):
  return render(request, 'myapp/landing.html', {})

def patient(request):
  return render(request, 'myapp/patient.html', {})

def profile(request):
  return render(request, 'myapp/profile.html', {})

def patient_detail(request):
  return render(request, 'myapp/detail.html', {})

def donor_views(request):
    form = DonorForm (request.POST or None)
    if form.is_valid():
        form.save()
    context = { 
        'form': form
     }
    return render(request, 'donor/donor_create.html', context)

# def home(TemplateView):
    # template = 'home/home.html'

    def get(self, request):
      form = PatientForm() (request.POST)
      return render(request, self.template_name, {'form':form})
      text = form.cleaned_data ['post']
      form = PatientForm
      return redirect ('home:home')

      args = {"form".form} ('text'.text)
      return render(request, self.template_name, args)

  
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

  