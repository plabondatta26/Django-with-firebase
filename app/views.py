from django.shortcuts import render
#from .models import Register
# Create your views here.
from firebase import firebase

def register(request):
    firebas = firebase.FirebaseApplication('https://clustered-data.firebaseio.com/', None)
    get_data = firebas.get('', None)
    print(get_data)

    time_list = []
    light_list = []
    cpu_list = []
    fan_list = []
    new_clusters_list = []

    for keys, values in enumerate(get_data):
        for key, value in enumerate(values):
            if value == 'Time':
                time_list.append(values[value])
            elif value == 'Light':
                light_list.append(values[value])
            elif value == 'Cpu':
                cpu_list.append(values[value])
            elif value == 'Fan':
                fan_list.append(values[value])
            elif value == 'new_clusters':
                new_clusters_list.append(values[value])
    



    return render(request, 'app/register.html', {'time_list': time_list})