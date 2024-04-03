from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import date
# Create your views here.

def LoadingHomePage(request):
    return render(request,"Admin/HomePage.html")


def District(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("txt_district"))
        return render(request,"Admin/District.html",{"District":data})
    else:
        return render(request,"Admin/District.html",{"District":data})

def DeleteDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("webadmin:District")

def Updatedis(request,uid):
    dis=tbl_district.objects.get(id=uid)
    if request.method=="POST":
        dis.district_name=request.POST.get("txt_district")
        dis.save()
        return redirect("webadmin:District")
    else:
        return render(request,"Admin/District.html",{"disdata":dis})
        
def Category(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("txt_category"))
        return render(request,"Admin/Category.html",{"Category":data})
    else:
        return render(request,"Admin/Category.html",{"Category":data})

def DeleteCategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("webadmin:Category")

def Updatecat(request,uid):
    cat=tbl_category.objects.get(id=uid)
    if request.method=="POST":
        cat.category_name=request.POST.get("txt_category")
        cat.save()
        return redirect("webadmin:Category")
    else:
        return render(request,"Admin/Category.html",{"catdata":cat})
          
def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Admin/Place.html",{'data':data})
    else:
        return render(request,"Admin/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("webadmin:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("webadmin:placeInsertSelect")
    else:
        return render(request,"Admin\Place.html",{"editdata":editdata,"districtdata":district})




        
def ProviderType(request):
    data=tbl_providertype.objects.all()
    if request.method=="POST":
        tbl_providertype.objects.create(providertype_name=request.POST.get("txt_providertype"))
        return render(request,"Admin/ProviderType.html",{"ProviderType":data})
    else:
        return render(request,"Admin/ProviderType.html",{"ProviderType":data})

def DeleteProviderType(request,did):
    tbl_providertype.objects.get(id=did).delete()
    return redirect("webadmin:ProviderType")

def Updatedis(request,uid):
    dis=tbl_providertype.objects.get(id=uid)
    if request.method=="POST":
        dis.providertype_name=request.POST.get("txt_providertype")
        dis.save()
        return redirect("webadmin:ProviderType")
    else:
        return render(request,"Admin/ProviderType.html",{"disdata":dis})






def FreelancerType(request):
    data=tbl_freelancertype.objects.all()
    if request.method=="POST":
        tbl_freelancertype.objects.create(freelancertype_name=request.POST.get("txt_freelancertype"))
        return render(request,"Admin/FreelancerType.html",{"FreelancerType":data})
    else:
        return render(request,"Admin/FreelancerType.html",{"FreelancerType":data})

def DeleteFreelancerType(request,did):
    tbl_freelancertype.objects.get(id=did).delete()
    return redirect("webadmin:FreelancerType")

def Updatedis(request,uid):
    dis=tbl_freelancertype.objects.get(id=uid)
    if request.method=="POST":
        dis.freelancertype_name=request.POST.get("txt_freelancertype")
        dis.save()
        return redirect("webadmin:FreelancerType")
    else:
        return render(request,"Admin/FreelancerType.html",{"disdata":dis})




def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Admin/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("webadmin:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("webadmin:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Admin/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Admin/UserListRejected.html",{"userdata":userdata})




def providerListNew(request):
    providerdata = tbl_provider.objects.filter(provider_status=0)
    return render(request,"Admin/ProviderListNew.html",{"providerdata":providerdata})

def acceptprovider(request,aid):
    provider = tbl_provider.objects.get(id=aid)
    provider.provider_status = 1
    provider.save()
    return redirect("webadmin:LoadingHomePage")

def rejectprovider(request,rid):
    provider = tbl_provider.objects.get(id=rid)
    provider.provider_status = 2
    provider.save()
    return redirect("webadmin:LoadingHomePage")

def providerListAccepted(request):
    providerdata = tbl_provider.objects.filter(provider_status=1)
    return render(request,"Admin/ProviderListAccepted.html",{"providerdata":providerdata})

def providerListRejected(request):
    providerdata = tbl_provider.objects.filter(provider_status=2)
    return render(request,"Admin/ProviderListRejected.html",{"providerdata":providerdata})



def freelancerListNew(request):
    freelancerdata = tbl_freelancer.objects.filter(freelancer_status=0)
    return render(request,"Admin/FreelancerListNew.html",{"freelancerdata":freelancerdata})

def acceptfreelancer(request,aid):
    freelancer = tbl_freelancer.objects.get(id=aid)
    freelancer.freelancer_status = 1
    freelancer.save()
    return redirect("webadmin:LoadingHomePage")

def rejectfreelancer(request,rid):
    freelancer = tbl_freelancer.objects.get(id=rid)
    freelancer.freelancer_status = 2
    freelancer.save()
    return redirect("webadmin:LoadingHomePage")

def freelancerListAccepted(request):
    freelancerdata = tbl_freelancer.objects.filter(freelancer_status=1)
    return render(request,"Admin/FreelancerListAccepted.html",{"freelancerdata":freelancerdata})

def freelancerListRejected(request):
    freelancerdata = tbl_freelancer.objects.filter(freelancer_status=2)
    return render(request,"Admin/FreelancerListRejected.html",{"freelancerdata":freelancerdata})




def ComplaintListNew(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"Admin/ComplaintListNew.html",{'userComplaint':userComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("webadmin:LoadingHomePage")
    else:
        return render(request,"Admin/ComplaintListReply.html",{'complaint':complaint})
    
def ComplaintSolved(request):
    userdata=tbl_user.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"Admin/ComplaintListSolved.html",{'userComplaint':userComplaint})
    

def UserFeedbackNew(request):
    data=tbl_feedback.objects.filter(feedback_status=0)
    return render(request,"Admin/UserFeedBack.html",{'data':data})



def adminInsertSelect(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        contact=request.POST.get('txtcontact')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtpwd')
        tbl_admin.objects.create(admin_name=name,admin_contact=contact,admin_email=email,admin_password=pwd)
        return redirect("webadmin:adminInsertSelect")
    else:
        return render(request,"Admin/AdminRegistration.html",{'data':data})

def delAdminReg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("webadmin:adminInsertSelect")

def adminRegUpdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_contact=request.POST.get("txtcontact")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpwd")
        editdata.save()
        return redirect("webadmin:adminInsertSelect")
    else:
        return render(request,"Admin\AdminRegistration.html",{"editdata":editdata})

