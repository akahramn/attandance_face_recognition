from django.urls import path
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:instructor_id>', views.instructor_home_page, name='home'),
    path('lessons/<int:lesson_id>', views.lesson, name='lesson'),
    path('lessons/<int:lesson_id>/takeAttendance', views.take_attendance, name='take_attendance'),
    path('lessons/<int:lesson_id>/attendances', views.attendances, name='attendances'),
    path('lessons/attendances/<int:attendance_id>', views.attendance_list, name='attendance_list'),
    path('test', views.test, name="test"),

]