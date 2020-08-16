from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from myapp import views
# from django.contrib.auth.views import login
from django.conf.urls.static import static
from django.conf import settings
 

urlpatterns = [
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('patient/', views.patient, name='patient'),
    #path('public_profile/<int:pk>', views.profile, name='dashboard'),
    #path('detail/<int:pk>', views.patient_detail, name='patient_dashboard'),
    path('donor/new', views.new_donor, name='new_donor'),
    path('instructions/', views.instructions, name='instructions'),

    #profile to dashboard Name
    
    path('dashboard/<int:pk>', views.dashboard, name='patient_dashboard'),

    #detail to profile name
    path('profile/<int:pk>', views.profile, name='profile'),

    path('responses/', views.responses, name='responses'),

    #path('list_patients/', views.list_patients, name='list_patients')

    # path('myapp/donor', myapp_views.donor_views, name='donor_views'),
    # path('myapp/add/', myapp_views.add_patient, name='add_patient'),
    # path('myapp.')

  ] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
