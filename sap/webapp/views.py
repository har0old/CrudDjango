from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

def bienvenido(request):   
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id') #order_by(id) para ordendar por el id
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas':personas})

