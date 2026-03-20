from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from .forms import UsuarioForm, UsuarioUpdate
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect       
from django.contrib.auth import authenticate, login


# Create your views here.


class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = "usuario_create.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario_list')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao cadastrar usuário. Verifique os dados informados.')
        return super().form_invalid(form)

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'
    context_object_name = 'usuarios'

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'usuario_update.html'
    form_class = UsuarioUpdate
    success_url = reverse_lazy('usuario_list') 

    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao atualizar usuário. Verifique os dados informados.')
        return super().form_invalid(form)

class UsuarioDeleteView(DeleteView):
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
        try:
            usuario = Usuario.objects.get(login=login, senha=senha)
        except Usuario.DoesNotExist:
            usuario = None
        if usuario is None:
            messages.error(request, 'Login ou senha inválidos.')
            return self.get(request, *args, **kwargs)

        messages.success(request, f'Bem-vindo, {usuario.nome}!')
        return redirect('index')
