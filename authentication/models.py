# models.py
from django.db import models

class Student(models.Model):
    s_name = models.CharField(max_length=200)
    s_fathername = models.CharField(max_length=200)
    s_mothername = models.CharField(max_length=200)
    s_addr = models.CharField(max_length=200)
    previous_school = models.CharField(max_length=200)  # Replaced s_school with previous_school
    s_phone = models.CharField(max_length=20, default='')  # Added New field for student's phone address
    s_gender = models.CharField(max_length=200)
    s_class = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "%s %s %s " % (self.s_name, self.s_fathername, self.s_phone)  # Display phone instead of email
