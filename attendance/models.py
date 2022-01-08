import datetime
from django.db import models
from jsonfield import JSONField

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


class Attendance(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    lesson_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson.name


