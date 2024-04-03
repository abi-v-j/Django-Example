from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"Freelancer/HomePage.html")

def my_pro(request):
    data=tbl_freelancer.objects.get(id=request.session["fid"])
    return render(request,"Freelancer/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_freelancer.objects.get(id=request.session["fid"])
    if request.method=="POST":
        prodata.freelancer_name=request.POST.get('txtname')
        prodata.freelancer_contact=request.POST.get('txtcon')
        prodata.freelancer_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Freelancer/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Freelancer/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_freelancer.objects.filter(id=request.session["fid"],freelancer_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                freelancerdata=tbl_freelancer.objects.get(id=request.session["fid"],freelancer_password=request.POST.get('txtcurpass'))
                freelancerdata.freelancer_password=request.POST.get('txtnewpass')
                freelancerdata.save()
                return render(request,"Freelancer/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Freelancer/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Freelancer/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Freelancer/ChangePassword.html")


#
def BookingListNew(request):
    userID=tbl_freelancer.objects.get(id=request.session["fid"])
    userdata = tbl_booking.objects.filter(booking_status=0,freelancer=userID)
    return render(request,"Freelancer/BookingListNew.html",{"userdata":userdata})

def acceptbooking(request,aid):
    user = tbl_booking.objects.get(id=aid)
    user.booking_status = 1
    user.save()
    return redirect("Freelancer:homepage")

def rejectbooking(request,rid):
    user = tbl_booking.objects.get(id=rid)
    user.booking_status = 2
    user.save()
    return redirect("Freelancer:homepage")


def BookingListAccepted(request):
    userID=tbl_freelancer.objects.get(id=request.session["fid"])
    userdata = tbl_booking.objects.filter(booking_status=1,freelancer=userID)
    return render(request,"Freelancer/BookingListAccepted.html",{"userdata":userdata})

def BookingListRejected(request):
    userID=tbl_freelancer.objects.get(id=request.session["fid"])
    userdata = tbl_booking.objects.filter(booking_status=2,freelancer=userID)
    return render(request,"Freelancer/BookingListRejected.html",{"userdata":userdata})
