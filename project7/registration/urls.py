from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    path('success/', lambda request: render(request, 'registration/success.html'), name='success'),
]