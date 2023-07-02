from django.contrib import admin
from .models import Producto,Mesa,Venta_mesa,Registro_ventas
# Register your models here.


admin.site.register(Producto)
admin.site.register(Mesa)
admin.site.register(Venta_mesa)
admin.site.register(Registro_ventas)

