from django.http import HttpResponse
from datetime import datetime

def current_datetime(request):
    now = datetime.now ()
    html=f"<html><body><h1>Current Date and Time:{now}</h1></body></html>"
    return HttpResponse(html)
