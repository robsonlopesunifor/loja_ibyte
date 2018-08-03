from django.shortcuts import render, redirect
from .form import PedidosForm
import requests

def pedidos(request, cliente):
    componente = {}
    payload = {'cliente':cliente}
    componente['componentes'] = requests.get("http://127.0.0.1:8000/pedidos_api",params=payload).json()
    return render(request, 'listagem.html', componente)

def pedir(request):
    form = PedidosForm(request.POST, None)
    if form.is_valid():
        postar(form)
        return redirect('pedidos', form.data['cliente'])
    return render(request, 'pedir.html', {'form': form})

def postar(form):
    payload = {
               "cliente": form.data["cliente"],
               "processadore": form.data["processadore"],
               "memoria_ram": form.data["memoria_ram"],
               "disco_rigido": form.data["disco_rigido"],
               "placa_de_video": form.data["placa_de_video"],
               "gabinete": form.data["gabinete"],
               "placa_mae": form.data["placa_mae"],
               "fone": form.data["fone"],
               "cartao_id":form.data["cartao_id"],
               "estatos": form.data["estatos"]
               }
    url = "http://127.0.0.1:8000/pedidos_api/"
    r = requests.post(url, data=payload)

