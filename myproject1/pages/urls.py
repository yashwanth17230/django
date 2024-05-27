from django.urls import path
from .views import Home_page_view
urlpatterns=[path("",Home_page_view,name="Home"),]