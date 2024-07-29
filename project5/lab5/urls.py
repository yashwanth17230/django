from django.urls import path
from . import views

urlpatterns = [
    path('',views.fruit_students_list,name='fruit_students_list'),
]