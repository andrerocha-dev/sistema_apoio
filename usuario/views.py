from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from .forms import UsuarioForm, UsuarioUpdate, UpdateSenha
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


# Create your views here.

class LoginRequiredMixin:
    """Mixin para garantir que o usuário esteja logado via sessão."""

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            messages.error(
                request, 'Acesso negado. Por favor, realize o login.')
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = "usuario_create.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Erro ao cadastrar usuário. Verifique os dados informados.')
        return super().form_invalid(form)


class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = 'usuarios'


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'usuario_update.html'
    form_class = UsuarioUpdate
    success_url = reverse_lazy('usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Erro ao atualizar usuário. Verifique os dados informados.')
        return super().form_invalid(form)


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Usuário deletado com sucesso!')
        return super().delete(request, *args, **kwargs)


class UsuarioLoginView(TemplateView):
    template_name = 'usuario_login.html'

    def post(self, request, *args, **kwargs):
        login = request.POST.get('login', '').strip()
        senha = request.POST.get('senha', '').strip()

        if not login or not senha:
            messages.error(request, 'Informe login e senha.')
            return self.get(request, *args, **kwargs)
        usuario = Usuario.objects.filter(login=login, senha=senha).first()
        if usuario is None:
            messages.error(request, 'Login ou senha inválidos.')
            return self.get(request, *args, **kwargs)
        else:
            request.session['logado'] = True
            request.session['usuario_id'] = usuario.id

        messages.success(request, f'Bem-vindo, {usuario.nome}!')
        return redirect('index')


class UsuarioUpdateSenha(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'usuario_update_senha.html'
    form_class = UpdateSenha
    success_url = reverse_lazy('usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Senha atualizada com sucesso!')
        return super().form_valid(form)


class UsuarioLogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        request.session.pop('logado', None)
        request.session.pop('usuario_id', None)
        messages.success(request, 'Você saiu do sistema com sucesso.')
        return redirect('usuario_login')
