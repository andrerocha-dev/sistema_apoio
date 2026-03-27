from django.urls import path
from .views import (
    ObraCreateView,
    ObraListView,
    ObraUpdateView,
    ObraDeleteView,
    PorEstadoCreateView,
    PorEstadoDeleteView,
    PorEstadoListView,
    PorEstadoUpdateView,
    ImplantacaoCreateView,
    ImplantacaoDeleteView,
    ImplantacaoListView,
    ImplantacaoUpdateView,
    ObrasAtivasCreateView,
    ObrasAtivasDeleteView,
    ObrasAtivasListView,
    ObrasAtivasUpdateView,
    ObrasDesativadasCreateView,
    ObrasDesativadasDeleteView,
    ObrasDesativadasListView,
    ObrasDesativadasUpdateView,

)

urlpatterns = [

    # Rotas para Obra
    path('criar/', ObraCreateView.as_view(), name='obra_create'),
    path('', ObraListView.as_view(), name='obra_list'),
    path('<int:pk>/editar/', ObraUpdateView.as_view(), name='obra_update'),
    path('<int:pk>/deletar/', ObraDeleteView.as_view(),
         name='obra_confirm_delete'),

    # Rotas para Por Estado
    path('por_estado/criar/', PorEstadoCreateView.as_view(),
         name='porestado_create'),
    path('por_estado/', PorEstadoListView.as_view(), name='porestado_list'),
    path('por_estado/<int:pk>/editar/',
         PorEstadoUpdateView.as_view(), name='porestado_update'),
    path('por_estado/<int:pk>/deletar/',
         PorEstadoDeleteView.as_view(), name='porestado_delete'),

    # Rotas para Implantação
    path('implantacao/criar/', ImplantacaoCreateView.as_view(),
         name='implantacao_create'),
    path('implantacao/', ImplantacaoListView.as_view(), name='implantacao_list'),
    path('implantacao/<int:pk>/editar/',
         ImplantacaoUpdateView.as_view(), name='implantacao_update'),
    path('implantacao/<int:pk>/deletar/',
         ImplantacaoDeleteView.as_view(), name='implantacao_delete'),

    # Rotas para Obras Ativas
     path('ativas/criar/', ObrasAtivasCreateView.as_view(),
           name='obrasativas_create'),            
     path('ativas/', ObrasAtivasListView.as_view(), name='obrasativas_list'),
     path('ativas/<int:pk>/editar/',
           ObrasAtivasUpdateView.as_view(), name='obrasativas_update'),
     path('ativas/<int:pk>/deletar/',
           ObrasAtivasDeleteView.as_view(), name='obrasativas_delete'), 
      
    # Rotas para Obras Desativadas
    path('desativadas/criar/', ObrasDesativadasCreateView.as_view(),
           name='obrasdesativadas_create'),            
     path('desativadas/', ObrasDesativadasListView.as_view(), name='obrasdesativadas_list'),
     path('desativadas/<int:pk>/editar/',
           ObrasDesativadasUpdateView.as_view(), name='obrasdesativadas_update'),
     path('desativadas/<int:pk>/deletar/',
           ObrasDesativadasDeleteView.as_view(), name='obrasdesativadas_delete'),
    



]
