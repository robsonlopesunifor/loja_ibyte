from clientes import views as clientes_views
from pedidos import views as pedidos_views
from produtos import views as produtos_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', clientes_views.cadastrar, name='cadastrar'),
    path('login/', clientes_views.login, name='login'),
    path('pedir/', pedidos_views.pedir, name='pedir'),
    path('pedidos/<int:cliente>/', pedidos_views.pedidos, name='pedidos'),
    path('processador/', produtos_views.processador, name='processador'),
    path('memoria_ram/', produtos_views.memoria_ram, name='memoria_ram'),
    path('disco_rigido/', produtos_views.disco_rigido, name='disco_rigido'),
    path('placa_de_video/', produtos_views.placa_de_video, name='placa_de_video'),
    path('gabinete/', produtos_views.gabinete, name='gabinete'),
    path('placa_mae/', produtos_views.placa_mae, name='placa_mae'),
    path('fone/', produtos_views.fone, name='fone'),
    path('lista_de_componentes/', produtos_views.listar, name='lista_de_componentes'),
]
