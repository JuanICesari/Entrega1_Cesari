from django.shortcuts import render

from .models import Verduras,Frutas,Fruto_Secos
from .forms import Verduras_formulario,Frutas_formulario,Fruto_Secos_formulario

# Create your views here.

def verduleria(request):
    return render(request, "verduleria.html") 



def agregar_modelo_verduras(request):
    if request.method == 'POST':
        form = Verduras_formulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            verduras = Verduras(nombre=data ['nombre'], tipo=data['tipo'], precio=data['precio'])
            verduras.save()
            return render(request, "index.html")

    form = Verduras_formulario()
    return render(request, "formulario_verdu.html", {"form": form}) 



def agregar_modelo_frutas(request):
    if request.method == 'POST':
        form = Frutas_formulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            frutas = Frutas(nombre=data ['nombre'], tipo=data['tipo'], precio=data['precio'])
            frutas.save()
            return render(request, "index.html")

    form = Frutas_formulario()
    return render(request, "formulario_fruta.html", {"form": form}) 



def agregar_modelo_frutos_secos(request):
    if request.method == 'POST':
        form = Fruto_Secos_formulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            frutos = Fruto_Secos(nombre=data ['nombre'], precio=data['precio'])
            frutos.save()
            return render(request, "index.html")

    form = Fruto_Secos_formulario()
    return render(request, "formulario_fruto_seco.html", {"form": form}) 
    
