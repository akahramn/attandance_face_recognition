from django.urls import path
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:instructor_id>', views.instructor_home_page, name='home'),
    path('lessons/<int:lesson_id>', views.lesson, name='lesson'),
    path('lessons/<int:lesson_id>/takeAttendance', views.take_attendance, name='take_attendance'),
    path('lessons/<int:lesson_id>/attendanceList', views.attendance_list, name='attendance_list'),




]