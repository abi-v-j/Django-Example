from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")

class tbl_freelancer(models.Model):
    freelancer_name=models.CharField(max_length=50)
    freelancer_contact=models.CharField(max_length=50)
    freelancer_email=models.CharField(max_length=50)
    freelancer_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    freelancertype = models.ForeignKey(tbl_freelancertype, on_delete=models.CASCADE)
    freelancer_photo = models.FileField(upload_to='Assets/FreeLancerDocs/')
    freelancer_proof = models.FileField(upload_to='Assets/FreeLancerDocs/')
    freelancer_status = models.IntegerField(default="0")

class tbl_provider(models.Model):
    provider_name=models.CharField(max_length=50)
    provider_contact=models.CharField(max_length=50)
    provider_email=models.CharField(max_length=50)
    provider_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    providertype=models.ForeignKey(tbl_providertype, on_delete=models.CASCADE)
    provider_photo = models.FileField(upload_to='Assets/UserPhoto/')
    provider_proof = models.FileField(upload_to='Assets/UserProof/')
    provider_status = models.IntegerField(default="0")
    