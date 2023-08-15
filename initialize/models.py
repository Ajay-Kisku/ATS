from django.db import models

class Discription(models.Model):
    disc = models.TextField()
    
class Pdf_upload(models.Model):
    name = models.CharField(max_length=50,default="xyz")    
    email = models.EmailField(max_length=400)
    skills = models.CharField(max_length=400,default="xyz")
    experience = models.CharField(max_length=400,default="xyz")
    score = models.FloatField(default=0)
    pdf = models.FileField(upload_to="pdfs/")
    q1 = models.CharField(max_length=1000,default=" ")
    q2 = models.CharField(max_length=1000,default=" ")
    q3 = models.CharField(max_length=1000,default=" ")
    q4 = models.CharField(max_length=1000,default=" ")
    q5 = models.CharField(max_length=1000,default=" ")
    a1 = models.CharField(max_length=1000,default=" ")
    a2 = models.CharField(max_length=1000,default=" ")
    a3 = models.CharField(max_length=1000,default=" ")
    a4 = models.CharField(max_length=1000,default=" ")
    a5 = models.CharField(max_length=1000,default=" ")
    

# Create your models here.
 