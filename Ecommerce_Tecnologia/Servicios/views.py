from django.shortcuts import render
from django.http import HttpResponse
from Servicios.models import Musico

# Create your views here.
#logica del backend

def vistaEjemplo(request):
    #request-> contiene la informacion de usuario
    #Envio de informacion:
    #get-> peticion de usuario  para acceder a una pagina web
    #post -> envio de informaion del usuario al servidor(aplicacion web)
    #Put-Patch-Delete

    Juanes=Musico.objects.get(nombreArtistico="Juanes")

    return HttpResponse("Estas en la aplicacion de Servicios " + Juanes.nombreArtistico)

