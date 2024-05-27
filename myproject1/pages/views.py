from django.shortcuts import render
from django.http import HttpResponse

def Home_page_view(Request):
    return HttpResponse("HELLO WORLD")

# Create your views here.
