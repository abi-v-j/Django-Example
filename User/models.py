from django.db import models
from Guest.models import *
from Provider.models import *
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE,null=True)
   

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)

class tbl_booking(models.Model):
    booking_postdate=models.DateField(auto_now_add=True)
    booking_fordate=models.CharField(max_length=500)
    booking_message=models.CharField(max_length=500)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    freelancer = models.ForeignKey(tbl_freelancer,on_delete=models.CASCADE,null=True)
    booking_status = models.IntegerField(default="0")

class tbl_application(models.Model):
    application_postdate=models.DateField(auto_now_add=True)
    application_resume=models.FileField(upload_to='Assets/UserResume/')
    application_message=models.CharField(max_length=500)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(tbl_job,on_delete=models.CASCADE,null=True)
    application_status = models.IntegerField(default="0")
    