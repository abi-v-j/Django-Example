from django.urls import path,include
from Admin import views
app_name="webadmin"
urlpatterns = [


    path('HomePage/',views.LoadingHomePage, name="LoadingHomePage"),
    
    path('District/',views.District, name="District"),
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('Updatedis/<int:uid>' , views.Updatedis,name="Updatedis"),


    path('Category/',views.Category, name="Category"),
    path('deletecategory/<int:did>',views.DeleteCategory,name="DeleteCategory"),
    path('Updatecat/<int:uid>' , views.Updatecat,name="Updatecat"),
    



    path('ProviderType/',views.ProviderType, name="ProviderType"),
    path('deleteprovidertype/<int:did>',views.DeleteProviderType,name="DeleteProviderType"),

  

    path('FreelancerType/',views.FreelancerType, name="FreelancerType"),
    path('deletefreelancertype/<int:did>',views.DeleteFreelancerType,name="DeleteFreelancerType"),
    

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),


    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),

    path('freelancerListNew/',views.freelancerListNew,name="freelancerListNew"),
    path('acceptfreelancer/<int:aid>',views.acceptfreelancer,name="acceptfreelancer"),
    path('rejectfreelancer/<int:rid>',views.rejectfreelancer,name="rejectfreelancer"),
    path('freelancerListAccepted/',views.freelancerListAccepted,name="freelancerListAccepted"),
    path('freelancerListRejected/',views.freelancerListRejected,name="freelancerListRejected"),


    path('providerListNew/',views.providerListNew,name="providerListNew"),
    path('acceptprovider/<int:aid>',views.acceptprovider,name="acceptprovider"),
    path('rejectprovider/<int:rid>',views.rejectprovider,name="rejectprovider"),
    path('providerListAccepted/',views.providerListAccepted,name="providerListAccepted"),
    path('providerListRejected/',views.providerListRejected,name="providerListRejected"),


    path('ComplaintListNew/',views.ComplaintListNew,name="ComplaintListNew"),
    path('ComplaintReply/<int:cid>',views.ComplaintReply,name="ComplaintReply"),
    path('ComplaintSolved/',views.ComplaintSolved,name="ComplaintSolved"),


    path('UserFeedbackNew/',views.UserFeedbackNew,name="UserFeedbackNew"),


    path('AdminRegistration/', views.adminInsertSelect,name="adminInsertSelect"),
    path('delAdminReg/<int:did>', views.delAdminReg,name="delAdminReg"),
    path('adminRegUpdate/<int:eid>',views.adminRegUpdate,name="adminRegUpdate"),
    
]
