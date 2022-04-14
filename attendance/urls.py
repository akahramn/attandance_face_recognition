from django.urls import path
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.login_page, name='login'),
    path('login_system', views.login_system, name='login_system'),
    path('<int:instructor_id>/home-page', views.instructor_home_page, name='home'),
    path('<int:instructor_id>/lessons', views.lessons, name='lessons'),
    path('lessons/<int:lesson_id>', views.lesson, name='lesson'),
    path('lessons/<int:lesson_id>/takeAttendance', views.take_attendance, name='take_attendance'),
    path('lessons/<int:lesson_id>/attendances', views.attendances, name='attendances'),
    path('lessons/attendances/<int:attendance_id>', views.attendance_list, name='attendance_list'),
    path('aboutus', views.about_us, name='about_us'),
    path('contactUs', views.contact_view, name='contact_us')

]