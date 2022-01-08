from django.db import models
from django import forms
from PIL import Image
import datetime
from django.contrib.auth.models import User

# Create your models here.
# 
course = [
    ('btch', 'B.TECH'),
    ('mtech', 'M.TCH'),
    ('mca', 'MCA'),
    ('bca','BCA'),
]


status = [
    ('pending', 'PENDING'),
    ('rejected', 'REJECTED'),
    ('selected', 'SELECTED'),
    
]

gendr = [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
]
  
class Student(models.Model):

    
    aplicationdoc = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    coursename = models.CharField(max_length=20,choices=course)
    studentname = models.CharField(max_length=100)
    
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    gender=models.CharField(max_length=20, choices=gendr )
    mono=models.CharField(max_length=100)
    emall=models.EmailField()
    dob = models.DateField()
    category = models.CharField(max_length=100)
    village=models.CharField(max_length=1000)
    distic=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    
    boardname=models.CharField(max_length=300)
    tenmarks=models.CharField(max_length=100)
    twmarks=models.CharField(max_length=100)
    twboard=models.CharField(max_length=100)
    graduation=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
   
 

    
   
    
    def __str__(self):
        return self.studentname

    
    


  
class Student_docoments(models.Model):
    docsid = models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True)
    photo=models.ImageField(upload_to='myimage/image')
    sign=models.ImageField(upload_to='myimage/sign')
    marksheet_10=models.FileField(upload_to='document_10',null=True)
    marksheet_12=models.FileField(upload_to='document_12',null=True)
    marksseet_graduation=models.FileField(upload_to='graduation_docs',null=True)

class Student_status(models.Model):
   
    statusid = models.OneToOneField(Student,on_delete=models.CASCADE,primary_key=True)
    status = models.CharField(max_length=300,choices=status)
    reason=models.CharField(max_length=1000)
    def __str__(self):
        return self.status
    

 
class Contact(models.Model):
    coursename = models.CharField(max_length=20,choices=course)
    contact_name = models.CharField(  max_length=50)
    contact_number = models.CharField(max_length=47)
    contact_email = models.EmailField()
    content = models.CharField(max_length=1000)
        
        
    
    

    
    
    
    
    