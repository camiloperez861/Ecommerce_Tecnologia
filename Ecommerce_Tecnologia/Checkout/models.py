from django.db import models

# Create your models here.

class CarritoCompras(models.Model):
    usuario=models.CharField(max_length=100)  #CharField-> Informacion en texto
    dcto=models.FloatField(default=0)  #FloatField ->permite alamcenar numeros decimales
    total=0                            #default -> define un valor por defecto (en caso de que no se defina)
    productosBD={
        'Jeans':10000,
        'Zapatos':50000
    }

class Producto(models.Model):
    opciones=(
        ("Mujer","M"),
        ("Hombre", "H")
    )
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    categoria=models.CharField(choices=opciones,max_length=10) #Choices-> tener una estructura que contenga diferentes opciones
    cod_barras=models.CharField(primary_key=True,max_length=100)

    def __str__(self):
        #Brindar una identificacion general en base de datos (seccion 'Admin')
        return self.nombre


class Item(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE) #Objeto de tipo producto
    carrito=models.ForeignKey(CarritoCompras,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=0)

    def __str__(self):
        return self.producto.nombre

    def subtotal(self):
        #subtotal=precioporoducto*cantidadproducto
        return self.producto.precio*self.cantidad

"""
SHELL

from Checkout.models import * 

#Creacion de Productos-> Una sola vez
Jeans=Producto.objects.create(nombre="Jeans",precio=100000,categoria="M",cod_barras="101")
Camisa=Producto.objects.create(nombre="Camisa",precio=50000,categoria="M",cod_barras="102")

#Desde la segunda vez->Obtener objetos de productos
Jeans=Producto.objects.get(nombre="Jeans")
Camisa=Producto.objects.get(nombre="Camisa")

--------------------------------------------------------------------------------------------------

#Crear carrito de compras->Una sola vez
car1=CarritoCompras.objects.create(usuario="1",dcto=0.0)
#Desde la segunda vez eb adelante-> obtener objeto de carrito de compras
car1=Producto.objects.get(usuario="1")

------------------------------------------------------------------------------------------------

#Crear item 
item=Item.objects.create(producto=Jeans,carrito=car1,cantidad=2)



"""






