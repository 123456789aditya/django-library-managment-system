from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    libid=models.CharField(max_length=4)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)