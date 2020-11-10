from django.shortcuts import render
#from .models import Register
# Create your views here.
from firebase import firebase

def register(request):
    firebas = firebase.FirebaseApplication('https://fatchdata-988cd.firebaseio.com/', None)

    # data = {
    #     'contact': 'hwsgfu',
    #     'name': 'hnfdsgfu'
    # }

    #result = firebas.post('/fatchdata-988cd/', data)
    g_data = {
        'contact': 'dg ',
        'name': 'saegeasr'
    }
    get_data = firebas.get('/fatchdata-988cd/', None)
    if get_data is 'contact':
        print(get_data)
    else:
        print("doesn't found")
    #print(result)
    print(get_data)
    return render(request, 'app/register.html')
