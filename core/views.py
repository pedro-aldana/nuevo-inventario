from inventory.models import Venta_mesa,Registro_ventas,Producto
from django.shortcuts import redirect,render,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import io
import base64
import matplotlib.pyplot as plt
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models import Max
from datetime import date, timedelta,datetime



def redireccionar_admin(request):
    url_admin = reverse('admin:index')  # Reemplaza 'admin:index' si la URL de administración es diferente
    return redirect(url_admin)


def graficas_ventas():
    ventas = Registro_ventas.objects.all()
    fechas = [venta.fecha for venta in ventas]
    montos = [venta.monto for venta in ventas]
    
    fig, ax = plt.subplots()
    ax.plot(fechas, montos)
    ax.set(xlabel='Fechas', ylabel='Montos', title='Ventas')
    ax.set_xticklabels(fechas, rotation=45)
    plt.tight_layout()

    # Convertir la gráfica a una cadena base64
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    
    return imagen_base64
   

@login_required
def HomeView(request):
    
    fecha_deseada = date.today()  # Fecha deseada (puedes usar cualquier fecha específica)
    fecha_inicio = fecha_deseada
    fecha_fin = fecha_deseada + timedelta(days=1)

    ganancias = Registro_ventas.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).aggregate(total_ganancias=Sum('monto'))

    total_ganancias = ganancias['total_ganancias']
    
    # suma de la cantidad de todos los productos
    cantidad_total = Producto.objects.aggregate(total_cantidad=Sum('cantidad'))
    
    # Productos mas vendidos
    productos_mas_vendidos = Registro_ventas.objects.annotate(total_ventas=Max('cantidad_v')).order_by('-total_ventas')[0:5]
    
    # Usuarios registrados
    usuarios_registrados = User.objects.count()
    
    # Suma de ganancias fecha por mes
    
    fecha_actual = datetime.now()
    # fecha de 30 dias
    fecha_deseada_mes = date.today()  # Fecha deseada (puedes usar cualquier fecha específica)
    fecha_inicio_mes = fecha_deseada_mes
    fecha_fin_mes = fecha_deseada_mes + timedelta(days=30)

    ganancias_mes = Registro_ventas.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).aggregate(total_ganancias_mes=Sum('monto'))

    total_ganancias_mes = ganancias_mes['total_ganancias_mes']
    
    # Grafica ventas
    graficas_venta = graficas_ventas

    context = {
        'total_ganancias': total_ganancias,
        'cantidad_total': cantidad_total,
        'productos_mas_vendidos': productos_mas_vendidos,
        'usuarios': usuarios_registrados,
        'total_ganancias_mes':total_ganancias_mes,
        'grafica_venta':graficas_venta
    }
    
    return render(request, 'pages/index.html', context)

