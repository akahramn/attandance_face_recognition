from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from attendance.models import Instructor, Student, Lesson
from .face_utils import recognize_faces, take_snap



def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    print(lesson)

    return render(request, 'attendance/lesson.html', {'lesson': lesson})


def instructor_home_page(request, instructor_id):
    instructor = Instructor.objects.filter(instructor_number=instructor_id)

    lessons = Lesson.objects.filter(instructor__name_lastname=instructor[0].name_lastname)


    return render(request, 'attendance/home_page.html', {'lessons': lessons})


def index(request):


    return render(request, 'attendance/index.html', {'attendance_list': attendance_list})


def take_attendance(request, lesson_id):
    take_snap()
    attendance_list = recognize_faces()

    #json_format = json.dumps(attendance_list)


    return HttpResponseRedirect(reverse('attendance:attendance_list', args=(attendance_list)))


def attendance_list(request, json_format):

    return render(request, 'attendance/attendance_list', {'attendance_list' : json_format})