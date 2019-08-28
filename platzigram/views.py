"""Platzi gram views"""
#django
from django.http import HttpResponse

#utilities
from datetime import datetime

def hello_world(request):
    """return a greeting"""
    now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server is {now}'.format(now=str(now)))

def hi(request):
    """hi"""
    numeros=request.GET['num']
    print(numeros)

#    import pdb;  pdb.set_trace() #esto detiene la ejecucion y permite la interaccion con la consola
    return HttpResponse(numeros)
