from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('ProviderRegistration/',views.ProviderRegistration,name="ProviderRegistration"),
    path('Freelancer/',views.FreelancerRegistration,name="FreelancerRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    
    path('Login/',views.Login,name="Login"),


    path('',views.Index,name="Index"),
]