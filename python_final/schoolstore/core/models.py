# core/models.py
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=255)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    # Add other fields as mentioned in the requirements

    def __str__(self):
        return self.user.username


class Material(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FormModel(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=10)
    materials_provide = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
