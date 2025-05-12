from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='account/')


class Subject(models.Model):
    name = models.CharField(max_length=50)

class LearningClass(models.Model):
    name = models.CharField(max_length=20)
    subjects = models.ManyToManyField(Subject)

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    learning_class = models.ForeignKey(LearningClass, on_delete=models.SET_NULL, null=True)
