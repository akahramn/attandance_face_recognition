from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from attendance.models import Instructor, Student, Lesson
from .face_utils import take_snap, recognize_faces


def index(request):
    take_snap()
    attendance_list = recognize_faces()
    #students = Student.objects.filter(student_number = 2)
    #print(students)

    return render(request, 'attendance/index.html', {'attendance_list': attendance_list})
