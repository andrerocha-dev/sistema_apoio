"""
URL configuration for cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

# IMPORTA A CLASSE DE VIEW
from cadastro.views import IndexTemplateView, PessoaCreateView, FaltasListView, FaltasCreateView, PessoaListView, PessoaUpdateView, PessoaDeleteView, PrestadorCreateView, PrestadorListView, PrestadorUpdateView, PrestadorDeleteView, AtrasosListView, AtrasosCreateView, AtrasosUpdateView, AtrasosDeleteView, FeriasListView, FeriasCreateView, FeriasUpdateView, FeriasDeleteView, CustoParceirosListView, CustoParceirosCreateView, CustoParceirosUpdateView, CustoParceirosDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),

    # RENDERIZAR A PÁGINA INICIAL
    path("", lambda request: redirect('/usuarios/login/')),
    
    
    
    # Rotas para Pessoas
    path('cadastro/index', IndexTemplateView.as_view(), name='index'),
    path('cadastro', PessoaCreateView.as_view(), name='cadastro'),
    path('faltas/', FaltasListView.as_view(), name='faltas_list'),
    path('faltas/create/', FaltasCreateView.as_view(), name='faltas_create'),
    path('pessoas/', PessoaListView.as_view(), name='pessoas_list'),
    path('atualiza_pessoas/<int:pk>/edit/',
         PessoaUpdateView.as_view(), name='pessoa_update'),
    path('pessoas/<int:pk>/delete/',
         PessoaDeleteView.as_view(), name='pessoa_delete'),
    
    # Rotas para Prestadores
    path('prestadores/create/', PrestadorCreateView.as_view(),
         name='prestador_create'),
    path('prestadores/', PrestadorListView.as_view(), name='prestadores_list'),
    path('prestadores/<int:pk>/edit/',
         PrestadorUpdateView.as_view(), name='prestador_update'),
    path('prestadores/<int:pk>/delete/',
         PrestadorDeleteView.as_view(), name='prestador_delete'),
    
    # Rotas para Atrasos
    path('atrasos/', AtrasosCreateView.as_view(), name='atrasos_create'),
    path('atrasos/list', AtrasosListView.as_view(), name='atrasos_list'),
    path('atrasos/<int:pk>/edit/',
         AtrasosUpdateView.as_view(), name='atrasos_update'),
    path('atrasos/<int:pk>/delete/',
         AtrasosDeleteView.as_view(), name='atrasos_delete'),
         
     # Rotas para Férias
     path('ferias/', FeriasListView.as_view(), name='ferias-list'),
     path('ferias/create/', FeriasCreateView.as_view(), name='ferias-create'),
     path('ferias/<int:pk>/edit/', FeriasUpdateView.as_view(), name='ferias-update'),
     path('ferias/<int:pk>/delete/', FeriasDeleteView.as_view(), name='ferias-delete'),
     
     # Rotas para Custo Parceiros
     path('custoparceiros/', CustoParceirosListView.as_view(), name='custoparceiros-list'),
     path('custoparceiros/create/', CustoParceirosCreateView.as_view(), name='custoparceiros-create'),
     path('custoparceiros/<int:pk>/edit/', CustoParceirosUpdateView.as_view(), name='custoparceiros-update'),
     path('custoparceiros/<int:pk>/delete/', CustoParceirosDeleteView.as_view(), name='custoparceiros-delete'),
     
     # Rota para cadastro de usuário
     path('usuarios/', include('usuario.urls')),
         
]
