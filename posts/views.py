
#
# from django.shortcuts import render
from django.shortcuts import render

#utilities
from datetime import datetime

# TEMP: creation of posts array
posts=[
    {
        'title':'Salud',
        'user':{
            'name':'Beimer campos Mezones',
            'picture':'https://picsum.photos/200/200/?image=1036'
        },
        'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=1036',

    },
    {
        'title':'Riqueza',
        'user':{
            'name':'Beimer campos Mezones',
            'picture':'https://picsum.photos/200/200/?image=903'
        },
        'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=903',

    },
    {
        'title':'Felicidad',
        'user':{
            'name':'Beimer campos Mezones',
            'picture':'https://picsum.photos/200/200/?image=883'
        },
        'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=883',

    },
]
def list_posts(request):
    return render(request,'feed.html',{'posts':posts})
# Create your views here.
