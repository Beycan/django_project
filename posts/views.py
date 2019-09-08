
#
# from django.shortcuts import render
from django.http import HttpResponse

#utilities
from datetime import datetime

# TEMP: creation of posts array
posts=[
    {
        'name':'Salud',
        'user':'Beimer campos',
        'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1036',

    },
    {
        'name':'Riqueza',
        'user':'Beimer campos',
        'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=903',

    },
    {
        'name':'Felicidad',
        'user':'Beimer campos',
        'timestamp':datetime.now().strftime('%b %dth,%Y - %H:%M hrs'),
        'picture':'https://picsum.photos/200/200/?image=1076',

    }
]
def list_posts(request):
    content=[]
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}" alt="no image" /></figure>
        """.format(**post))
    return HttpResponse('<br />'.join(content))
# Create your views here.
