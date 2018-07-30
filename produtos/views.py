from django.shortcuts import render
from .models import Processadore
from .models import Memoria_ram
from .models import Disco_rigido
from .models import Placa_de_video
from .models import Gabinete
from .models import Placa_mae
from .models import Fone
from .form import ProcessadoreForm
from .form import Memoria_ramForm
from .form import Disco_rigidoForm
from .form import Placa_de_videoForm
from .form import GabineteForm
from .form import Placa_maeForm
from .form import FoneForm

def listar(request):
    dados = {}
    componente = {}
    componente['processador'] = []
    componente['memoria_ram'] = []
    componente['disco_rigido'] = []
    componente['placa_de_video'] = []
    componente['gabinete'] = []
    componente['placa_mae'] = []
    componente['fone'] = []

    processador = Processadore.objects.all()
    memoria_ram = Memoria_ram.objects.all()
    disco_rigido = Disco_rigido.objects.all()
    placa_de_video = Placa_de_video.objects.all()
    gabinete = Gabinete.objects.all()
    placa_mae = Placa_mae.objects.all()
    fone = Fone.objects.all()

    """
    for dado in processador:
        componente['processador'].append({'nome':dado.nome,'estoque':dado.estoque})
    
    for dado in memoria_ram:
        componente['memoria_ram'].append({'nome':dado.nome,'estoque':dado.estoque})
    for dado in disco_rigido:
        componente['disco_rigido'].append({'nome':dado.nome,'estoque':dado.estoque})
    for dado in placa_de_video:
        componente['placa_de_video'].append({'nome':dado.nome,'estoque':dado.estoque})
    for dado in gabinete:
        componente['gabinete'].append({'nome':dado.nome,'estoque':dado.estoque})
    for dado in placa_mae:
        componente['placa_mae'].append({'nome':dado.nome,'estoque':dado.estoque})
    for dado in fone:
        componente['fone'].append({'nome':dado.nome,'estoque':dado.estoque})
    """
    return render(request, 'listar_componentes.html', {'componentes':componente})

def processador(request):
    form = ProcessadoreForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'processador.html', {'form': form})

def memoria_ram(request):
    form = Memoria_ramForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'memoria_ram.html', {'form': form})

def disco_rigido(request):
    form = Disco_rigidoForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'disco_rigido.html', {'form': form})

def placa_de_video(request):
    form = Placa_de_videoForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'placa_de_video.html', {'form': form})

def gabinete(request):
    form = GabineteForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'gabinete.html', {'form': form})

def placa_mae(request):
    form = Placa_maeForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'placa_mae.html', {'form': form})

def fone(request):
    form = FoneForm(request.POST, None)
    if form.is_valid():
        form.save()
    return render(request, 'fone.html', {'form': form})

