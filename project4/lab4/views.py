from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta

def hello(request):
    return HttpResponse("Hello World!")

def current_datatime(request):
    now=datetime.now()
    html=f"<html><body>Current Date and Time:{now}</body></html>"
    return HttpResponse(html)

def hours_ahead(request,hours):
    try:
        hours=int(hours)

    except ValueError:
        return HttpResponse("Inavlid hour parameter",status=400)
    dt=datetime.now()+timedelta(hours=hours)
    
    html=f"<html><body>In{hours}hours(s),it will be{dt}.</body></html>"
    return HttpResponse(html)

def hours_before(request,hours):
    try:
        hours=int(hours)

    except ValueError:
        return HttpResponse("Inavlid hour parameter",status=400)
    dt=datetime.now()-timedelta(hours=hours)
    html=f"<html><body>In{hours}hours(s),it will be{dt}.</body></html>"
    return HttpResponse(html)