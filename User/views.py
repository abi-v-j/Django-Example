from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Admin.models import *
from Provider.models import *
# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")

#
def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('txttitle')
        details=request.POST.get('txtcomplaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/POSTComplaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")


def UserFeedback(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        subject=request.POST.get('txtsubject')
        details=request.POST.get('txtfeedback')
        tbl_feedback.objects.create(feedback_subject=subject,feedback_details=details,user=userID)
        return redirect("User:UserFeedback")
    else:
        return render(request,"User/UserFeedback.html",{"data":data})
   

def delFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:UserFeedback")

#
def freelancerList(request):
    userdata = tbl_freelancer.objects.filter(freelancer_status=1)
    return render(request,"User/SearchFreeLancer.html",{"userdata":userdata})

def bookFreelancer(request,did):
    editdata=tbl_freelancer.objects.get(id=did)
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_booking.objects.create(user=userID,booking_fordate=request.POST.get("txtdate"),booking_message=request.POST.get("txtmsg"),freelancer=editdata)
        return redirect("User:homepage")
    else:
        return render(request,"User\BookFreelancerNow.html",{"userdata":editdata})

def freelancerBookingListNew(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_booking.objects.filter(user=userID,booking_status=0)
    return render(request,"User/freelancerBookingListNew.html",{"userdata":userdata})

def freelancerBookingListAccepted(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_booking.objects.filter(user=userID,booking_status=1)
    return render(request,"User/freelancerBookingListAccepted.html",{"userdata":userdata})

def freelancerBookingListRejected(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    userdata = tbl_booking.objects.filter(user=userID,booking_status=2)
    return render(request,"User/freelancerBookingListRejected.html",{"userdata":userdata})


#
def SearchJob(request):
    category = tbl_category.objects.all()
    data = tbl_job.objects.filter(job_status='1')
    if request.method=="POST":
        category = tbl_category.objects.get(id=request.POST.get('sel_type'))
        data = tbl_job.objects.filter(category=category)
        return render(request,"User/SearchJob.html",{"data":data})
    else:
        return render(request,"User/SearchJob.html",{"category":category,"data":data})


def applyJob(request,did):
    editdata=tbl_job.objects.get(id=did)
    userID=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        tbl_application.objects.create(application_resume=request.FILES.get("fileresume"),user=userID,application_message=request.POST.get("txtmsg"),job=editdata)
        return redirect("User:homepage")
    else:
        return render(request,"User\ApplyJobNow.html",{"userdata":editdata})


def JobListApplied(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_application.objects.filter(application_status='0',user=userID)
    return render(request,"User/JobListApplied.html",{"data":data})

def JobListAccepted(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_application.objects.filter(application_status='1',user=userID)
    return render(request,"User/JobListAccepted.html",{"data":data})

def JobListRejected(request):
    userID=tbl_user.objects.get(id=request.session["uid"])
    data = tbl_application.objects.filter(application_status='2',user=userID)
    return render(request,"User/JobListRejected.html",{"data":data})