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

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    return HttpResponse(str(numbers), content_type='application/json')