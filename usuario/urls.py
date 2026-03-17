from django.urls import path
from .views import (
    UsuarioCreateView,
    UsuarioListView,
    UsuarioUpdateView,
    UsuarioDeleteView,
)

urlpatterns = [
    path('criar/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('', UsuarioListView.as_view(), name='usuario_list'),
    path('<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/deletar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
]
