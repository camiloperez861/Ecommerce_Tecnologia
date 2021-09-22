from django.db import models

# Create your models here.
#Crud- Conexion con base de datos. Manipular bases de datos mediante clases Python

"""
Beat E-> Proyecto musical.
Musico-albunes-canciones

models.Model -> clase con la cual se establece la conexion crud -> tabla sql

models.CharField-> campos de texto tipo sql

null=True -> permite argumentos de tipo 'NULL'
blank=True -> permite argumentos vacios

ForeignKey-> establecer conexion entre tablas SQL

on_delete=models.CASCADE-> eliminar Todos los albunes que le correspondan al musico que se haya eliminado

models.TimeField() -> Almacenamiento de formato de tiempo
"""

class Musico (models.Model):
    nombre=models.CharField(max_length=100,null=True,blank=True)
    apellido=models.CharField(max_length=100,null=True,blank=True)
    nombreArtistico=models.CharField(max_length=100)

    def __str__(self):
        #Especificamos que se va a mostrar
        return self.nombreArtistico




class Album(models.Model):
    musico=models.ForeignKey(Musico, on_delete=models.CASCADE) #Establece conexion entre la tbla SQL 'Album' y la tabla 'Musico'
    nombre=models.CharField(max_length=100)
    caratula=models.ImageField(null=True,blank=True)
    fechaCreacion=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.nombre


class Canciones(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    duracion=models.TimeField(null=True,blank=True)
    archivoAudio=models.FileField(null=True,blank=True)

    def __str__(self):
        return self.nombre



"""SQL
Create table Servicios_Musico(
    id integer primary key autoincrement,
    nombre Varchar(100) not null 
);
"""


"""
SHELL -> Permite ejecutar codigo Python del poryecto Django
    python manage.py shell

    Se puede hacer:
    -Probar codigo CRUD
    -Probar la logica de un algoritmo
    Sistema de depuracion de codigo

    from Servicios.models import *

    #Obtener informacion
    musicos=Musico.objects.all()  -> Obtener todos los registros de la tabla 'Musico' en base de datos 
    Juanes= Musico.objects.get(nombreArtistico="Juanes")  get-> esperamos como respuesta un objeto

    albumesJuanes=Album.objects.filter(musico=Juanes) -> filter -> esperamos multiples objetos
    

    #Crear un nuevo musico
    Shakira=Musico.objects.create(nombreArtistico="Shakira")

    #Crear nuevo Album
    nuevoAlbum= Album.objects.create(musico=Juanes,nombre="Ordinario")
"""





