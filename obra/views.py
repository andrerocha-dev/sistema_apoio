from django.contrib import messages

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from usuario.views import LoginRequiredMixin

# Create your views here.
from .models import Obra, PorEstado, Implantacao, ObrasAtivas, ObrasDesativadas
from .forms import ObraForm, PorEstadoForm, ImplantacaoForm, ObrasAtivasForm, ObrasDesativadasForm


# ========================= VIEWS PARA OBRA ========================#

class ObraCreateView(LoginRequiredMixin, CreateView):
    model = Obra
    template_name = 'obra_create.html'
    form_class = ObraForm
    success_url = reverse_lazy('obra_list')

    def form_valid(self, form):
        messages.success(self.request, 'Obra criada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar obra. Verifique os dados.')
        return super().form_invalid(form)


class ObraListView(LoginRequiredMixin, ListView):
    model = Obra
    template_name = 'obra_list.html'
    context_object_name = 'obras'
    ordering = ['nome']


class ObraUpdateView(LoginRequiredMixin, UpdateView):
    model = Obra
    template_name = 'obra_update.html'
    form_class = ObraForm
    success_url = reverse_lazy('obra_list')

    def form_valid(self, form):
        messages.success(self.request, 'Obra atualizada com sucesso!')
        return super().form_valid(form)


class ObraDeleteView(LoginRequiredMixin, DeleteView):
    model = Obra
    template_name = 'obra_confirm_delete.html'
    success_url = reverse_lazy('obra_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Obra deletada com sucesso!')
        return super().delete(request, *args, **kwargs)

# ================== Fim das views para obra ==================#

# ========================= VIEWS PARA POR ESTADO ========================#


class PorEstadoCreateView(LoginRequiredMixin, CreateView):
    model = PorEstado
    template_name = 'porestado_create.html'
    form_class = PorEstadoForm
    success_url = reverse_lazy('porestado_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Erro ao criar registro. Verifique os dados.')
        return super().form_invalid(form)


class PorEstadoListView(LoginRequiredMixin, ListView):
    model = PorEstado
    template_name = 'porestado_list.html'
    context_object_name = 'porestado'
    ordering = ['nome']


class PorEstadoUpdateView(LoginRequiredMixin, UpdateView):
    model = PorEstado
    template_name = 'porestado_update.html'
    form_class = PorEstadoForm
    success_url = reverse_lazy('porestado_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form)


class PorEstadoDeleteView(LoginRequiredMixin, DeleteView):
    model = PorEstado
    template_name = 'porestado_delete.html'
    success_url = reverse_lazy('porestado_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)

# ================== Fim das views para por estado ==========================#


class ImplantacaoCreateView(LoginRequiredMixin, CreateView):
    model = Implantacao
    template_name = 'implantacao_create.html'
    form_class = ImplantacaoForm
    success_url = reverse_lazy('implantacao_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Erro ao criar implantação. Verifique os dados.')
        return super().form_invalid(form)


class ImplantacaoListView(LoginRequiredMixin, ListView):
    model = Implantacao
    template_name = 'implantacao_list.html'
    context_object_name = 'implantacoes'
    ordering = ['ticket']


class ImplantacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Implantacao
    template_name = 'implantacao_update.html'
    form_class = ImplantacaoForm
    success_url = reverse_lazy('implantacao_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form)


class ImplantacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Implantacao
    template_name = 'implantacao_delete.html'
    success_url = reverse_lazy('implantacao_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)

# ================== Fim das views para implantação ==========================#

# ========================= VIEWS PARA OBRAS ATIVAS ========================#


class ObrasAtivasCreateView(LoginRequiredMixin, CreateView):
    model = ObrasAtivas
    template_name = 'obrasativas_create.html'
    form_class = ObrasAtivasForm
    success_url = reverse_lazy('obrasativas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Erro ao criar obra ativa. Verifique os dados.')
        return super().form_invalid(form)


class ObrasAtivasListView(LoginRequiredMixin, ListView):
    model = ObrasAtivas
    template_name = 'obrasativas_list.html'
    context_object_name = 'obrasativas'
    ordering = ['nome__nome']


class ObrasAtivasUpdateView(LoginRequiredMixin, UpdateView):
    model = ObrasAtivas
    template_name = 'obrasativas_update.html'
    form_class = ObrasAtivasForm
    success_url = reverse_lazy('obrasativas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form)


class ObrasAtivasDeleteView(LoginRequiredMixin, DeleteView):
    model = ObrasAtivas
    template_name = 'obrasativas_delete.html'
    success_url = reverse_lazy('obrasativas_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)

# ================== Fim das views para obras ativas ==========================#

# ========================= VIEWS PARA OBRAS DESATIVADAS ========================#


class ObrasDesativadasCreateView(LoginRequiredMixin, CreateView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_create.html'
    form_class = ObrasDesativadasForm
    success_url = reverse_lazy('obrasdesativadas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Erro ao criar obra desativada. Verifique os dados.')
        return super().form_invalid(form)


class ObrasDesativadasListView(LoginRequiredMixin, ListView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_list.html'
    context_object_name = 'obrasdesativadas'
    ordering = ['nome__nome']


class ObrasDesativadasUpdateView(LoginRequiredMixin, UpdateView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_update.html'
    form_class = ObrasDesativadasForm
    success_url = reverse_lazy('obrasdesativadas_list')

    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form)


class ObrasDesativadasDeleteView(LoginRequiredMixin, DeleteView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_delete.html'
    success_url = reverse_lazy('obrasdesativadas_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)

# ================== Fim das views para obras desativadas ==========================#
