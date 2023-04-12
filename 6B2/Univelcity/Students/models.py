from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    people = [
        ("m", "Male"),
        ("f", "Female")
    ]
    gender = models.CharField(max_length=1, choices=people)
    email = models.EmailField()
    cohort = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=11)