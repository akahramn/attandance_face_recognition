import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Instructor(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    name_lastname = models.CharField(max_length=50)
    instructor_number = models.IntegerField()

    def __str__(self):
        return self.name_lastname



class Student(models.Model):
    name_lastname = models.CharField(max_length=50)
    student_number = models.IntegerField()

    def __str__(self):
        return self.name_lastname


class Lesson(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    lesson_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson.name


