from django.urls import path
from User import views
app_name="User"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),

    path('UserFeedback/', views.UserFeedback, name='UserFeedback'),
    path('delFeedback/<int:did>',views.delFeedback,name="delFeedback"),

    path('freelancerList/',views.freelancerList,name="freelancerList"),
    path('bookFreelancer/<int:did>', views.bookFreelancer,name="bookFreelancer"),
    path('freelancerBookingListNew/',views.freelancerBookingListNew,name="freelancerBookingListNew"),
    path('freelancerBookingListAccepted/',views.freelancerBookingListAccepted,name="freelancerBookingListAccepted"),
    path('freelancerBookingListRejected/',views.freelancerBookingListRejected,name="freelancerBookingListRejected"),

    path('SearchJob/',views.SearchJob,name="SearchJob"),
    path('applyJob/<int:did>', views.applyJob,name="applyJob"),
    path('JobListApplied/',views.JobListApplied,name="JobListApplied"),
    path('JobListAccepted/',views.JobListAccepted,name="JobListAccepted"),
    path('JobListRejected/',views.JobListRejected,name="JobListRejected"),

]