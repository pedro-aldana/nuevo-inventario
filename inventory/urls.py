from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('productos/', views.Productos, name="productos"),
    path('productos/agregar/', views.agregar, name="agregar"),
    path('productos/editar/<int:id>', views.edit, name="edit"),
    path('eliminar/<int:id>',views.delete_2, name="delete_2"),
    
    
    # Ventas
    path('ventas/', views.ventas, name="ventas"),
    path('ventas/reporte', views.generar_reporte, name="reporte"),
    path('ventas/vender/', views.vender, name="vender"),
    
    
    # Mesas
    path('mesas/', views.mesas, name="mesas"),
    path('mesas/agregar/', views.agregar_mesas, name="agregar_mesas"),
    path('mesa/<int:mesa_id>/', views.detail, name="detail"),
    path('delete/<int:id>',views.delete, name="delete"),
    
]
   

