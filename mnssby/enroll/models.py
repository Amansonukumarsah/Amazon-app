from django.db import models

# Create your models here.
class studentdetails(models.Model):
    Institute_State=models.CharField(max_length=70)
    Institute_District=models.CharField(max_length=70)
    Name_of_Collage=models.CharField(max_length=70)
    Name_of_university=models.CharField(max_length=70)
    Institute_Type=models.CharField(max_length=70)
    Institute_City=models.CharField(max_length=70)
    Institute_pincode=models.CharField(max_length=70)
    Institute_Email_id=models.CharField(max_length=70)
    Institute_Mobile_No=models.IntegerField()
    pdf=models.FileField(upload_to='pdfs/')

class payment(models.Model):
    pdf=models.FileField(upload_to='pdfs/')
    pdf1=models.FileField(upload_to='pdfs/')
    
    
class feedback(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    feed_back=models.TextField(max_length=500)