import datetime
from django.db import models

from django.utils import timezone


class Instructor(models.Model):
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


