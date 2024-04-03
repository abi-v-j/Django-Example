from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.

def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})

def ProviderRegistration(request):
    district = tbl_district.objects.all()
    typeid = tbl_providertype.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        typeid = tbl_providertype.objects.get(id=request.POST.get('sel_type'))
        tbl_provider.objects.create(provider_name=request.POST.get("txtname"),provider_contact=request.POST.get("txtcontact"),provider_email=request.POST.get("txtemail"),provider_photo=request.FILES.get("fileImage"),provider_proof=request.FILES.get("fileProof"),provider_password=request.POST.get("txtpwd"),place=place,providertype=typeid)
        return redirect("Guest:ProviderRegistration")
    else:
        return render(request,"Guest/ProviderRegistration.html",{"districtdata":district,"typeid":typeid})

def FreelancerRegistration(request):
    district = tbl_district.objects.all()
    typeid = tbl_freelancertype.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        typeid = tbl_freelancertype.objects.get(id=request.POST.get('sel_type'))
        tbl_freelancer.objects.create(freelancertype=typeid,freelancer_name=request.POST.get("txtname"),freelancer_contact=request.POST.get("txtcontact"),freelancer_email=request.POST.get("txtemail"),freelancer_photo=request.FILES.get("fileImage"),freelancer_proof=request.FILES.get("fileProof"),freelancer_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:FreelancerRegistration")
    else:
        return render(request,"Guest/Freelancer.html",{"districtdata":district,"typeid":typeid})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})

def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        providercount = tbl_provider.objects.filter(provider_status='1',provider_email=request.POST.get("txt_email"),provider_password=request.POST.get("txt_password")).count() 
        freelancercount = tbl_freelancer.objects.filter(freelancer_status='1',freelancer_email=request.POST.get("txt_email"),freelancer_password=request.POST.get("txt_password")).count()   
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()           
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")

        elif providercount > 0:
            provider = tbl_provider.objects.get(provider_email=request.POST.get("txt_email"),provider_password=request.POST.get("txt_password"))
            request.session["pid"] = provider.id
            request.session["pname"] = provider.provider_name
            return redirect("Provider:homepage")
            
        elif freelancercount > 0:
            freelancer = tbl_freelancer.objects.get(freelancer_email=request.POST.get("txt_email"),freelancer_password=request.POST.get("txt_password"))
            request.session["fid"] = freelancer.id
            request.session["fname"] = freelancer.freelancer_name
            return redirect("Freelancer:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            return redirect("webadmin:LoadingHomePage")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")





def Index(request):
    return render(request,"Guest/index.html")