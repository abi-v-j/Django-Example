from django.urls import path
from Freelancer import views

app_name="Freelancer"

urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),

    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),


    path('BookingListNew/',views.BookingListNew,name="BookingListNew"),
    path('acceptbooking/<int:aid>',views.acceptbooking,name="acceptbooking"),
    path('rejectbooking/<int:rid>',views.rejectbooking,name="rejectbooking"),
    path('BookingListAccepted/',views.BookingListAccepted,name="BookingListAccepted"),
    path('BookingListRejected/',views.BookingListRejected,name="BookingListRejected"),
    

]