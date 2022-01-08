from django.contrib import admin

from .models import Instructor, Student, Lesson, Attendance

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Attendance)
