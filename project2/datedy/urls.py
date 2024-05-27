from django.urls import path
from.import views

urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('time/',views.current_datatime,name='current_time'),
    path('another-time-page/',views.current_datatime,name='another_time_page'),
    path('time/plus/<int:hours>/',views.hours_ahead,name='hours_ahead'),
    path('time/minus/<int:hours>/',views.hours_ahead,name='hours_ahead'),
]