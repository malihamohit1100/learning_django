from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50, verbose_name = "Student Name")
    roll = models.IntegerField(unique = True)
    age = models.IntegerField(null = True)
    father_name = models.CharField(max_length = 50, null = True, blank = True)
