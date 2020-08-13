"""mmfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from myapp import views
# from django.contrib.auth.views import login
 

urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('patient/', views.patient),
    path('profile/', views.profile),
     path('detail/<int:pk>', views.patient_detail),
    path('donor/new', views.new_donor, name='new_donor'),

    # path('myapp/donor', myapp_views.donor_views, name='donor_views'),
    # path('myapp/add/', myapp_views.add_patient, name='add_patient'),
    # path('myapp.')
]
