from django.urls import path
from .views import (
    UsuarioCreateView,
    UsuarioListView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    UsuarioLoginView,   # <-- adiciona aqui
)
urlpatterns = [
    path('criar/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('', UsuarioListView.as_view(), name='usuario_list'),
    path('<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/deletar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    path('login/', UsuarioLoginView.as_view(), name='usuario_login'),  # <-- nova rota
]
