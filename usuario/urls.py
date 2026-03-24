from django.urls import path
from .views import (
    UsuarioCreateView,
    UsuarioListView,
    UsuarioUpdateView,
    UsuarioDeleteView,
    UsuarioLoginView,   # <-- adiciona aqui
    UsuarioLogoutView,
    UsuarioUpdateSenha
)
urlpatterns = [
    path('criar/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('', UsuarioListView.as_view(), name='usuario_list'),
    path('<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_update'),
    path('<int:pk>/deletar/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    path('login/', UsuarioLoginView.as_view(), name='usuario_login'),  # <-- nova rota
    path('logout/', UsuarioLogoutView.as_view(), name='usuario_logout'),
    path('<int:pk>/editar_senha/', UsuarioUpdateSenha.as_view(), name='usuario_update_senha'),
]
