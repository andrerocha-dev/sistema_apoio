from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from usuario.models import Usuario
from usuario.views import LoginRequiredMixin
from .forms import PessoaForm, FaltasForm, PrestadorForm, AtrasosForm, FeriasForm
from .models import Pessoa, Faltas, Prestador, Atrasos, Ferias, CustoParceiros
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.

# Define a view class QUE CHAMA OS TEMPLATES


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count_pessoas'] = Pessoa.objects.count()
        context['count_prestadores'] = Prestador.objects.count()
        context['count_faltas'] = Faltas.objects.count()
        context['count_atrasos'] = Atrasos.objects.count()
        context['count_ferias'] = Ferias.objects.count()
        context['count_custos'] = CustoParceiros.objects.count()
        context['count_usuarios'] = Usuario.objects.count()
        # verificar se o usuário está logado
        usuario_id = self.request.session.get('usuario_id')
        if usuario_id:
            context['usuario'] = Usuario.objects.filter(id=usuario_id).first()
        return context


# ===========================FALTAS================================


class FaltasListView(LoginRequiredMixin, ListView):
    model = Faltas
    template_name = 'faltas_list.html'
    context_object_name = 'faltas'
    ordering = ['-data_falta']


class FaltasCreateView(LoginRequiredMixin, CreateView):
    model = Faltas
    template_name = 'faltas_create.html'
    form_class = FaltasForm
    success_url = reverse_lazy('faltas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Falta registrada com sucesso!')
        return super().form_valid(form)

# ============================PESSOAS==================================

# COLABORADORES


class PessoaCreateView(LoginRequiredMixin, CreateView):
    model = Pessoa
    template_name = "pessoa_create.html"
    form_class = PessoaForm
    success_url = reverse_lazy('cadastro')

    def form_valid(self, form):
        messages.success(self.request, 'Cadastro realizado com sucesso!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_pessoas'] = Pessoa.objects.order_by('-id')[:5]
        return context


class PessoaListView(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'pessoas_list.html'
    context_object_name = 'pessoas'
    ordering = ['nome']
    paginate_by = 9

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(nome__icontains=q) |
                Q(documento__icontains=q) |
                Q(funcao__icontains=q)
            )
        return qs.order_by('nome')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


class PessoaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pessoa
    template_name = 'pessoa_update.html'
    form_class = PessoaForm
    success_url = reverse_lazy('pessoas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cadastro atualizado com sucesso!')
        return super().form_valid(form)


class PessoaDeleteView(LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'pessoa_confirm_delete.html'
    success_url = reverse_lazy('pessoas_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Cadastro excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

# ==============================PRESTADOR=============================


class PrestadorCreateView(LoginRequiredMixin, CreateView):
    model = Prestador
    template_name = 'prestador_create.html'
    fields = ['nome']
    success_url = reverse_lazy('prestadores_list')

    def form_valid(self, form):
        messages.success(self.request, 'Prestador cadastrado com sucesso!')
        return super().form_valid(form)


class PrestadorListView(LoginRequiredMixin, ListView):
    model = Prestador
    template_name = 'prestadores_list.html'
    context_object_name = 'prestadores'
    ordering = ['nome']


class PrestadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Prestador
    template_name = 'prestador_update.html'
    form_class = PrestadorForm
    success_url = reverse_lazy('prestadores_list')

    def form_valid(self, form):
        messages.success(self.request, 'Prestador atualizado com sucesso!')
        return super().form_valid(form)


class PrestadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Prestador
    template_name = 'prestador_confirm_delete.html'
    success_url = reverse_lazy('prestadores_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Prestador excluído com sucesso!')
        return super().delete(request, *args, **kwargs)
# =================================ATRASOS===================================


class AtrasosCreateView(LoginRequiredMixin, CreateView):
    model = Atrasos
    template_name = 'atrasos_create.html'
    form_class = AtrasosForm
    success_url = reverse_lazy('atrasos_list')

    def form_valid(self, form):
        messages.success(self.request, 'Atraso registrado com sucesso!')
        return super().form_valid(form)


class AtrasosListView(LoginRequiredMixin, ListView):
    model = Atrasos
    template_name = 'atrasos_list.html'
    context_object_name = 'atrasos'
    ordering = ['-data_atraso']


class AtrasosUpdateView(LoginRequiredMixin, UpdateView):
    model = Atrasos
    template_name = 'atrasos_update.html'
    form_class = AtrasosForm
    success_url = reverse_lazy('atrasos_list')

    def form_valid(self, form):
        messages.success(self.request, 'Atraso atualizado com sucesso!')
        return super().form_valid(form)


class AtrasosDeleteView(LoginRequiredMixin, DeleteView):
    model = Atrasos
    template_name = 'atrasos_confirm_delete.html'
    success_url = reverse_lazy('atrasos_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Atraso excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

# ==============================FERIAS===================================


class FeriasCreateView(LoginRequiredMixin, CreateView):
    model = Ferias
    template_name = 'ferias_create.html'
    form_class = FeriasForm
    success_url = reverse_lazy('ferias-list')

    def form_valid(self, form):
        messages.success(self.request, 'Férias registradas com sucesso!')
        return super().form_valid(form)


class FeriasListView(LoginRequiredMixin, ListView):
    model = Ferias
    template_name = 'ferias_list.html'
    context_object_name = 'ferias'
    ordering = ['nome']


class FeriasUpdateView(LoginRequiredMixin, UpdateView):
    model = Ferias
    template_name = 'ferias_update.html'
    form_class = FeriasForm
    success_url = reverse_lazy('ferias-list')

    def form_valid(self, form):
        messages.success(self.request, 'Férias atualizadas com sucesso!')
        return super().form_valid(form)


class FeriasDeleteView(LoginRequiredMixin, DeleteView):
    model = Ferias
    template_name = 'ferias_confirm_delete.html'
    success_url = reverse_lazy('ferias-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Férias excluídas com sucesso!')
        return super().delete(request, *args, **kwargs)

# ============================CUSTO PARCEIROS===================================


class CustoParceirosCreateView(LoginRequiredMixin, CreateView):
    model = CustoParceiros
    template_name = 'custoparceiros_create.html'
    fields = ['nome', 'hora_tecnica', 'hora_adcional', 'remanejamento',
              'instalacao_1_catraca', 'instalacao_2_catracas', 'desmobilizacao']
    success_url = reverse_lazy('custoparceiros-list')

    def form_valid(self, form):
        messages.success(
            self.request, 'Custo Parceiro registrado com sucesso!')
        return super().form_valid(form)


class CustoParceirosListView(LoginRequiredMixin, ListView):
    model = CustoParceiros
    template_name = 'custoparceiros_list.html'
    context_object_name = 'custos'
    ordering = ['-id']


class CustoParceirosUpdateView(LoginRequiredMixin, UpdateView):
    model = CustoParceiros
    template_name = 'custoparceiros_update.html'
    fields = ['nome', 'hora_tecnica', 'hora_adcional', 'remanejamento',
              'instalacao_1_catraca', 'instalacao_2_catracas', 'desmobilizacao']
    success_url = reverse_lazy('custoparceiros-list')

    def form_valid(self, form):
        messages.success(
            self.request, 'Custo Parceiro atualizado com sucesso!')
        return super().form_valid(form)


class CustoParceirosDeleteView(LoginRequiredMixin, DeleteView):
    model = CustoParceiros
    template_name = 'custoparceiros_confirm_delete.html'
    success_url = reverse_lazy('custoparceiros-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Custo Parceiro excluído com sucesso!')
        return super().delete(request, *args, **kwargs)
