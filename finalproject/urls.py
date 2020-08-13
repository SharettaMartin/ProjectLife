

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from myapp import views
# from django.contrib.auth.views import login
 

urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('profile/', views.profile),
    path('detail/<int:pk>', views.patient_detail),
    path('patient/', views.patient, name='patient'),
    #path('public_profile/<int:pk>', views.profile, name='dashboard'),
    #path('detail/<int:pk>', views.patient_detail, name='patient_dashboard'),
    path('donor/new', views.new_donor, name='new_donor'),
    path('instructions/', views.instructions, name='instructions'),
    path('dashboard/<int:pk>', views.dashboard, name='patient_dashboard'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('responses/', views.responses, name='responses'),

   ]
