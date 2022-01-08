import datetime
import json
from datetime import date, timedelta
from django.db.models import Q

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from attendance.models import Instructor, Student, Lesson, Attendance
from .face_utils import recognize_faces, take_snap


def index(request):

    return render(request, 'attendance/index.html')


def lesson(request, lesson_id):

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'attendance/lesson.html', {'lesson': lesson})


def instructor_home_page(request, instructor_id):
    instructor = Instructor.objects.filter(instructor_number=instructor_id)

    lessons = Lesson.objects.filter(instructor__name_lastname=instructor[0].name_lastname)

    return render(request, 'attendance/home_page.html', {'lessons': lessons})


def take_attendance(request, lesson_id):
    #take_snap()
    attendance_list = recognize_faces()
    lesson = Lesson.objects.filter(pk=lesson_id)
    lesson_attendance = Attendance.objects.create(instructor=lesson[0].instructor, lesson=lesson[0])
    print("DERS SAATİ=", lesson_attendance.lesson_date)

    for student_name in attendance_list:
        student = Student.objects.filter(name_lastname=student_name)
        lesson_attendance.students.add(student[0])
        return render(request, 'attendance/attendance_list.html', {'attendance_list': attendance_list})



def attendances(request, lesson_id):
    #order_by('-pub_date')[:5]
    lesson = Lesson.objects.filter(pk=lesson_id)
    attendances = Attendance.objects.filter(lesson=lesson[0])
    return render(request, 'attendance/lesson_attendance.html', {'attendances': attendances})


def attendance_list(request, attendance_id):
    attendance = Attendance.objects.filter(pk=attendance_id)
    print("ATTENDANCE=", attendance)

    contex = attendance[0].students.all()
    return render(request, 'attendance/attendance_list.html', {'students': contex, 'attendance': attendance[0]})


def test(request):

    return render(request, 'attendance/test.html')