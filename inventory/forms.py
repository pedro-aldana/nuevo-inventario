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
    mesaId = forms.ModelChoiceField(queryset=Mesa.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Venta_mesa
        fields = ('producto','cantidad_vendida','mesaId')
        
    
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label=None, widget=forms.Select(attrs={
        'class': INPUT_CLASS,
    }))
    
    # mesaId = forms.ModelChoiceField(queryset=Mesa.objects.all(),widget=forms.Select(attrs={
    #     'class': INPUT_CLASS,
    #     'mesaId':forms.HiddenInput(),
        
        
    # }))
    
    cantidad_vendida = forms.CharField(widget=forms.NumberInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'ej: 30'
    })) 
    
    
              
        
    

class MesaForm(ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'
        
    nombre_mesa = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'ej: Mesa 1'
    }))        
    