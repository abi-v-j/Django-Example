from django.shortcuts import render,redirect
from Guest.models import *
from Provider.models import *
from User.models import *
# Create your views here.

def homepage(request):
    return render(request,"Provider/HomePage.html")

def my_pro(request):
    data=tbl_provider.objects.get(id=request.session["pid"])
    return render(request,"Provider/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_provider.objects.get(id=request.session["pid"])
    if request.method=="POST":
        prodata.provider_name=request.POST.get('txtname')
        prodata.provider_contact=request.POST.get('txtcon')
        prodata.provider_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Provider/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Provider/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_provider.objects.filter(id=request.session["pid"],provider_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                providerdata=tbl_provider.objects.get(id=request.session["pid"],provider_password=request.POST.get('txtcurpass'))
                providerdata.provider_password=request.POST.get('txtnewpass')
                providerdata.save()
                return render(request,"Provider/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Provider/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Provider/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Provider/ChangePassword.html")


#
def jobRegistration(request):
    category = tbl_category.objects.all()
    provider=tbl_provider.objects.get(id=request.session["pid"])
    if request.method=="POST":
        category = tbl_category.objects.get(id=request.POST.get('sel_type'))
        tbl_job.objects.create(job_details=request.POST.get("txtdetails"),job_name=request.POST.get("txtname"),job_contact=request.POST.get("txtcontact"),job_email=request.POST.get("txtemail"),job_lastdate=request.POST.get("txtdate"),job_salaryscale=request.POST.get("txtscale"),job_minqual=request.POST.get("txtqual"),category=category,provider=provider)
        return redirect("Provider:jobRegistration")
    else:
        return render(request,"Provider/JobDetails.html",{"category":category})


def jobListNew(request):
    provider=tbl_provider.objects.get(id=request.session["pid"])
    providerdata = tbl_job.objects.filter(job_status=0,provider=provider)
    return render(request,"Provider/JobListNew.html",{"providerdata":providerdata})

def deletejob(request,did):
    tbl_job.objects.get(id=did).delete()
    return redirect("Provider:homepage")


def acceptjob(request,aid):
    provider = tbl_job.objects.get(id=aid)
    provider.job_status = 1
    provider.save()
    return redirect("Provider:homepage")

def rejectjob(request,rid):
    provider = tbl_job.objects.get(id=rid)
    provider.job_status = 2
    provider.save()
    return redirect("Provider:homepage")

def jobListActive(request):
    provider=tbl_provider.objects.get(id=request.session["pid"])
    providerdata = tbl_job.objects.filter(job_status=1,provider=provider)
    return render(request,"Provider/JobListActive.html",{"providerdata":providerdata})

def jobListInactive(request):
    provider=tbl_provider.objects.get(id=request.session["pid"])
    providerdata = tbl_job.objects.filter(job_status=2,provider=provider)
    return render(request,"Provider/JobListInActive.html",{"providerdata":providerdata})

#
def JobListApplied(request):
    userID=tbl_provider.objects.get(id=request.session["pid"])
    data = tbl_application.objects.filter(application_status='0',job__provider=userID)
    return render(request,"Provider/JobListApplied.html",{"data":data})

def JobListAccepted(request):
    userID=tbl_provider.objects.get(id=request.session["pid"])
    data = tbl_application.objects.filter(application_status='1',job__provider=userID)
    return render(request,"Provider/JobListAccepted.html",{"data":data})

def JobListRejected(request):
    userID=tbl_provider.objects.get(id=request.session["pid"])
    data = tbl_application.objects.filter(application_status='2',job__provider=userID)
    return render(request,"Provider/JobListRejected.html",{"data":data})


def acceptappln(request,aid):
    provider = tbl_application.objects.get(id=aid)
    provider.application_status = 1
    provider.save()
    return redirect("Provider:homepage")

def rejectappln(request,rid):
    provider = tbl_application.objects.get(id=rid)
    provider.application_status = 2
    provider.save()
    return redirect("Provider:homepage")
