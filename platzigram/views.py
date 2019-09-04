"""Platzi gram views"""
#django
from django.http import HttpResponse

#utilities
from datetime import datetime
import json

def hello_world(request):
    """return a greeting"""
    now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server is {now}'.format(now=str(now)))

def sort_integers(request):
    """hi"""
    numeros=request.GET['num']
    numeros=[int(i) for i in numeros.split(',')]
    numeros=sorted(numeros)
    data={
        'status':'ok',
        'numbers':numeros,
        'mensaje':'este es el mensaje'
    }
    print(numeros)
    # import pdb;  pdb.set_trace()

#    import pdb;  pdb.set_trace() #esto detiene la ejecucion y permite la interaccion con la consola
    return HttpResponse(
        json.dumps(data,indent=4),
        content_type='application/json'
    )

def say_hi(request,name,age):
    """return a greeting"""
    if age <12:
        message="Sorry {}, you are not allowed here.".format(name)
    else:
        message="Hello, {}! Welcome to platzigram".format(name)

    return HttpResponse(message)
