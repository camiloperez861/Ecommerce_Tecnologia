from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#logica del backend

def vistaEjemplo(request):
    #request-> contiene la informacion de usuario
    #Envio de informacion:
    #get-> peticion de usuario  para acceder a una pagina web
    #post -> envio de informaion del usuario al servidor(aplicacion web)
    #Put-Patch-Delete

    return HttpResponse("Estas en la aplicacion de Servicios")

