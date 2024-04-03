from django.urls import path
from Provider import views

app_name="Provider"

urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('jobRegistration/',views.jobRegistration,name="jobRegistration"),
    path('jobListNew/',views.jobListNew,name="jobListNew"),
    path('deletejob/<int:did>',views.deletejob,name="deletejob"),
    path('acceptjob/<int:aid>',views.acceptjob,name="acceptjob"),
    path('rejectjob/<int:rid>',views.rejectjob,name="rejectjob"),
    path('jobListActive/',views.jobListActive,name="jobListActive"),
    path('jobListInactive/',views.jobListInactive,name="jobListInactive"),

    path('JobListApplied/',views.JobListApplied,name="JobListApplied"),
    path('JobListAccepted/',views.JobListAccepted,name="JobListAccepted"),
    path('JobListRejected/',views.JobListRejected,name="JobListRejected"),
    path('acceptappln/<int:aid>',views.acceptappln,name="acceptappln"),
    path('rejectappln/<int:rid>',views.rejectappln,name="rejectappln"),

]