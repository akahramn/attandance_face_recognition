from django.shortcuts import get_object_or_404, render, redirect, reverse
from attendance.models import Instructor, Student, Lesson, Attendance
from .face_utils import recognize_faces, take_snap


def lessons(request, instructor_id):
    instructor = Instructor.objects.filter(pk=instructor_id)
    lessons = Lesson.objects.filter(instructor=instructor[0])

    return render(request, 'attendance/lessons.html', {'lessons': lessons})


def lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'attendance/lesson.html', {'lesson': lesson})


def instructor_home_page(request, instructor_id):
    instructor = Instructor.objects.filter(pk=instructor_id)
    return render(request, 'attendance/home_page.html')


def take_attendance(request, lesson_id):
    take_snap()
    attendance_list = recognize_faces()
    lesson = Lesson.objects.filter(pk=lesson_id)
    lesson_attendance = Attendance.objects.create(instructor=lesson[0].instructor, lesson=lesson[0])
    print("ATTENDANCE=", attendance_list)

    for student_name in attendance_list:
        student = Student.objects.filter(name_lastname=student_name)
        print("STUDENT=", student)
        lesson_attendance.students.add(student[0])
    return render(request, 'attendance/lesson.html', {'alert_flag': True})


def attendances(request, lesson_id):
    lesson = Lesson.objects.filter(pk=lesson_id)
    attendances = Attendance.objects.filter(lesson=lesson[0])
    return render(request, 'attendance/lesson_attendance.html', {'attendances': attendances})


def attendance_list(request, attendance_id):
    attendance = Attendance.objects.filter(pk=attendance_id)
    contex = attendance[0].students.all()
    return render(request, 'attendance/attendance_list.html', {'students': contex, 'attendance': attendance[0]})


def login_page(request):

    return render(request, 'attendance/login_page.html')


def login_system(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        instructor = Instructor.objects.filter(username=username, password=password)
        request.session['username'] = instructor[0].name_lastname
        request.session['instructor_id'] = instructor[0].id

        if instructor:
            return redirect(reverse('attendance:home', args=[instructor[0].id]))


def about_us(request):

    return render(request, 'attendance/about_us.html')


def contact_view(request):

    return render(request, 'attendance/contact.html')