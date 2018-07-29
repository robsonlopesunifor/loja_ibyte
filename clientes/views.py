from clientes.models import Cliente
from django.shortcuts import render, redirect
from .form import ClienteForm
from django.contrib.auth.forms import AuthenticationForm

def cadastrar(request):
    data = {}
    form = ClienteForm(request.POST,request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'cadastrar.html', {'form': form})

def login(request):
    nome = 'null'
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        clientes = Cliente.objects.filter(nome=form.data['username'],
                                          senha=form.data['password'])
        for cliente in clientes:
            return redirect('pedidos',cliente.id)

    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})