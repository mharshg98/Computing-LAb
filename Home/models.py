from django.db import models
from django.utils import timezone
# Create your models here.

class Announcement(models.Model):
    time = models.DateTimeField(default = timezone.now)
    file = models.FileField(upload_to = 'annoncementfile')
    title =models.CharField(max_length=80)
    desc =models.CharField(max_length=200)
    subtitle =models.CharField(max_length=80)

    def __str__(self):
        return self.title

class Enroll_Data(models.Model):
    sheet_id = models.AutoField(primary_key = True)
    date = models.DateTimeField(default = timezone.now)
    enroll_datasheet = models.FileField(upload_to = 'enroll_datasheets')

class RegisteredStudents(models.Model):
    choices = ( ("CIVIENG" , "CIVIENG"), ("COMPENG" , "COMPENG"), ("ECIENG", "ECIENG"), ("ECTELEG", "ECTELEG"), ("ITENG", "ITENG"), ("MECHENG", "MECHENG"),  )
    choices1 = ( ("BTECH" , "BTECH"), ("MTECH" , "MTECH"))
    id=models.AutoField(primary_key=True)
    branch=models.CharField(choices = choices,max_length=100)
    course=models.CharField(choices = choices1,max_length=100)
    Reg_no=models.CharField(unique=True,max_length=10)
    roll_no=models.CharField(unique=True,max_length=10)
    name=models.CharField(max_length=100)
    session=models.CharField(null=True,max_length=100)
    email=models.EmailField(unique=True,null=True)
    mobile=models.CharField(null=True,max_length=10)

    def __str__(self):
        return self.Reg_no

class FrontImage(models.Model):
    id = models.AutoField(primary_key = True)
    title=models.CharField(max_length=100,default=' ')
    date = models.DateTimeField(default = timezone.now)
    image = models.ImageField(upload_to = 'FrontImage')

from django.contrib.auth.models import User
class Student(models.Model):
    id=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    choices = ( ("CIVIENG" , "CIVIENG"), ("COMPENG" , "COMPENG"), ("ECIENG", "ECIENG"), ("ECTELEG", "ECTELEG"), ("ITENG", "ITENG"), ("MECHENG", "MECHENG"),  )
    choices1 = ( ("BTECH" , "BTECH"), ("MTECH" , "MTECH"))
    branch=models.CharField(choices = choices,max_length=100)
    course=models.CharField(choices = choices1,max_length=100)
    Reg_no=models.CharField(unique=True,max_length=10)
    roll_no=models.CharField(unique=True,max_length=10)
    name=models.CharField(max_length=100)
    session=models.CharField(null=True,max_length=100)
    email=models.EmailField(unique=True,null=True)
    mobile=models.CharField(null=True,max_length=10)
    address=models.CharField(null=True,max_length=100)

    def __str__(self):
        return self.Reg_no


