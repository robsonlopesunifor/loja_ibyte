from clientes import views as clientes_views
from pedidos import views as pedidos_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', clientes_views.cadastrar, name='cadastrar'),
    path('login/', clientes_views.login, name='login'),
    path('pedir/', pedidos_views.pedir, name='pedir'),
    path('pedidos/<int:cliente>/', pedidos_views.pedidos, name='pedidos'),
]
