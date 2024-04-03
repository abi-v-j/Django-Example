from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
    
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    Subcategory_name=models.CharField(max_length=100)

class tbl_complainttype(models.Model):
    ComplaintType_name=models.CharField(max_length=100)

class tbl_providertype(models.Model):
    providertype_name=models.CharField(max_length=50)

class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)

class tbl_freelancertype(models.Model):
    freelancertype_name=models.CharField(max_length=50)

class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=100)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)


