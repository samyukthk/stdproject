from django.db import models

# Create your models here.

# University
class University(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Batch
class Batch(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    batch = models.CharField(max_length=100)
    Year = models.DateField()

    def __str__(self):
        return self.batch 

#student
class Student(models.Model):
    GENDER = (('MALE','MALE'),('FEMALE','FEMALE'))
    Batch = models.ForeignKey(Batch,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=GENDER)
    dob = models.DateField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return self.name