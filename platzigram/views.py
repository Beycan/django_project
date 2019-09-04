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

def hi(request):
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
    return HttpResponse(json.dumps(data,indent=4),content_type='application/json')
