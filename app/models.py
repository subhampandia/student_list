# Create your models here.
from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    student_class = models.CharField(max_length=20)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5)