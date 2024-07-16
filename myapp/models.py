from django.db import models

# Create your models here.
class User_data(models.Model):
    email=models.CharField(max_length=70)
    password=models.CharField(max_length=70)
    def __str__(self):
        return self.email
    
class Doctorinfor(models.Model):
    doctor_name = models.CharField(max_length=1000)
    doctor_image=models.ImageField(upload_to='doctor/')
    specialist= models.CharField(max_length=1000)

    def __str__(self):
        return self.doctor_name
    
class Registerinfo(models.Model):
    doctor_name=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    contact=models.IntegerField()
    problem=models.CharField(max_length=100)
    def __str__(self):
        return self.p_name