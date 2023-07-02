from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=3)
    cantidad = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
    

class Mesa(models.Model):
    nombre_mesa = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nombre_mesa



class Venta_mesa(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    mesaId = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    monto_mesa = models.DecimalField(max_digits=8, decimal_places=3,default=0,blank=True)
    fecha_venta = models.DateField()  
    
    def __str__(self) -> str:
        return f"Venta de: {self.producto.nombre} en la {self.mesaId.nombre_mesa}"
    
    def calcular_monto(self):
        return self.producto.precio * self.cantidad_vendida
    
    def clean(self):
        self.monto_mesa = self.calcular_monto()
        super().clean()
    
    
    
    def save(self, *args, **kwargs):
        if self.cantidad_vendida > self.producto.cantidad:
            raise ValueError("La cantidad vendida supera la cantidad disponible en el inventario.")
        super(Venta_mesa, self).save(*args, **kwargs)   
    
    
class Registro_ventas(models.Model):
    nombre = models.CharField(max_length=100,blank=True)
    cantidad_v = models.IntegerField(blank=True)
    monto = models.DecimalField(max_digits=8,decimal_places=3,default=0)
    fecha = models.DateField(blank=True)   
    
    
    def __str__(self) -> str:
        return self.nombre 
    




@receiver(post_save, sender=Venta_mesa)
def actualizar_inventario(sender, instance, created, **kwargs):
    if created:
        producto = instance.producto
        producto.cantidad -= instance.cantidad_vendida
        producto.save()    


@receiver(post_save, sender=Venta_mesa)
def auto_llenado_handler(sender, instance, created, **kwargs):
    if created:
        nombre_destino = instance.producto.nombre
        cantidad_destino = instance.cantidad_vendida
        monto_destino = instance.monto_mesa
        fecha_destino = instance.fecha_venta
        Registro_ventas.objects.create(nombre=nombre_destino,cantidad_v=cantidad_destino,monto=monto_destino,fecha=fecha_destino)
        
            