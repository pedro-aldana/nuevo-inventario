from django.forms import ModelForm
from django import forms
from .models import Producto,Venta_mesa,Mesa,Registro_ventas

INPUT_CLASS = 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-indigo-500'


class ProductForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={
        'class' : INPUT_CLASS,
        'placeholder': 'ej: Gaseosa'
    }))
    
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'ej: $2,500'
    }))
       
    cantidad = forms.CharField(widget=forms.NumberInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'ej: 30'
    }))


class VentasForm(ModelForm):
    class Meta:
        model = Venta_mesa
        fields = '__all__'
        
    
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label=None, widget=forms.Select(attrs={
        'class': INPUT_CLASS,
    }))
    
    mesaId = forms.ModelChoiceField(queryset=Mesa.objects.all(), empty_label=None, widget=forms.Select(attrs={
        'class': INPUT_CLASS,
    })) 
    
    cantidad_vendida = forms.CharField(widget=forms.NumberInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'ej: 30'
    })) 
    
    fecha_venta = forms.DateField(widget=forms.DateInput(attrs={
        'class': INPUT_CLASS,
        'type': 'date'
    }))
              
        
    

class MesaForm(ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'
        
    nombre_mesa = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'ej: Mesa 1'
    }))        
    