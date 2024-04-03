from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.


class tbl_job(models.Model):
    job_name=models.CharField(max_length=50)
    job_contact=models.CharField(max_length=50)
    job_email=models.CharField(max_length=50)
    job_details=models.CharField(max_length=500)
    job_lastdate=models.CharField(max_length=500)
    job_minqual=models.CharField(max_length=500)
    job_salaryscale=models.CharField(max_length=500)
    category = models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    job_status = models.IntegerField(default="0")
    provider=models.ForeignKey(tbl_provider, on_delete=models.CASCADE)