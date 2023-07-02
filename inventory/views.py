from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from .models import Producto,Mesa,Venta_mesa,Registro_ventas
from .forms import ProductForm,VentasForm,MesaForm
from openpyxl import Workbook
# Create your views here.

# Reporte

def generar_reporte(request):
    ventas = Registro_ventas.objects.all()
    
    wb = Workbook()
    ws = wb.active
    ws['B1'] = 'REPORTE DE VENTAS'
    
    ws.merge_cells('B1:E1')
    
    ws['B2'] = 'FECHA'
    ws['C2'] = 'PRODUCTO'
    ws['D2'] = 'CANTIDAD_V'
    ws['E2'] = 'MONTO'
    
    
    cont = 3
    
    for venta in ventas:
        ws.cell(row = cont, column = 2).value = venta.fecha
        ws.cell(row = cont, column = 3).value = venta.nombre
        ws.cell(row = cont, column = 4).value = venta.cantidad_v
        ws.cell(row = cont, column = 5).value = venta.monto
        cont+=1
    
    nombre_archivo = 'ReporteVentas.xlsx'
    response = HttpResponse(content_type = 'application/ms-excel')
    content = "attachament; filename = {0}".format(nombre_archivo)
    response['Content-Disposition'] = content
    wb.save(response)
    return response    


# vISTAS DE PRODUCTOS
@login_required
def Productos(request):
    
    productos = Producto.objects.filter(nombre__contains=request.GET.get('search', ''))
    
    context = {
        'productos': productos
    }
    
    
    return render(request, 'pages/productos.html', context)



@login_required
def agregar(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('inventory:productos')
    
    else:    
    
        form = ProductForm()
        context = {
            'form':form
        }
        return render(request, 'pages/crud/añadir.html', context)
    

def edit(request,id):
    
    producto = Producto.objects.get(id=id)
    
    if request.method == 'GET':
        form = ProductForm(instance= producto)
        context ={
            'form':form,
            'id': id
        }
        return render(request, 'pages/crud/editar.html', context)
        
    if request.method == 'POST':
        form = ProductForm(request.POST, instance= producto)
        if form.is_valid():
            form.save()
        
        context = {
            'form':form,
            'id':id
        }
        messages.success(request, 'Producto actualizado correctamente')
        return render(request, 'pages/crud/editar.html',context) 
    
    
def delete_2(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('inventory:productos') 
    

# VISTAS DE VENTAS
@login_required
def ventas(request):
    
    ventas = Registro_ventas.objects.filter(nombre__contains=request.GET.get('search', ''))
    
    context = {
        'ventas':ventas
    }
    
    return render(request, 'pages/ventas.html', context)

@login_required
def vender(request):
    try:
    
        if request.method == 'POST':
            form = VentasForm(request.POST)
            
            if form.is_valid():
                form.save()
            
            return redirect('inventory:ventas')
        
        else:
            
            form = VentasForm()
            context = {
                'form':form
            }
            return render(request, 'pages/crud/vender.html', context)        
    except ValueError as e:
        error_message = str(e)
        return  render(request, 'messages/error.html', {
            'error_message': error_message
        })   


# VISTAS DE MESAS
@login_required
def mesas(request):
    
    mesa = Mesa.objects.all()
    
    context = {
        'mesas':mesa
    }
    return render(request, 'pages/mesas.html',context)

@login_required
def agregar_mesas(request):
    
    if request.method == 'POST':
        form = MesaForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        return redirect('inventory:mesas')
    
    else:    
    
        form = MesaForm()
        context = {
            'form':form
        }
        return render(request, 'pages/crud/ag_mesa.html',context)
    
    

@login_required
def detail(request, mesa_id):
    
    mesa = get_object_or_404(Mesa, id=mesa_id)
    ventas = Venta_mesa.objects.filter(mesaId=mesa)
    
    

    context = {
        'mesa': mesa,
        'ventas':ventas,
        
    }
    
    return render(request, 'pages/detail.html',context)    

@login_required
def delete(request,id):
    venta_mesa = Venta_mesa.objects.get(id=id)
    venta_mesa.delete()
    return redirect('inventory:mesas')
