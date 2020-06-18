"""Michigram views"""

#django
from django.http import HttpResponse

#datetime
from datetime import datetime

def hello_world(request):
   

    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    
    ))

def hi(request):

   
    return HttpResponse('Hi!')