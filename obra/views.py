from pyexpat.errors import messages
from django.contrib import messages

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

# Create your views here.
from .models import Obra, PorEstado, Implantacao, ObrasAtivas, ObrasDesativadas
from .forms import ObraForm, PorEstadoForm, ImplantacaoForm, ObrasAtivasForm, ObrasDesativadasForm


#========================= VIEWS PARA OBRA ========================#

class ObraCreateView(CreateView):
    model = Obra
    template_name = 'obra_create.html'
    form_class = ObraForm
    success_url = reverse_lazy('obra_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Obra criada com sucesso!')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class ObraListView(ListView):
    model = Obra
    template_name = 'obra_list.html'
    context_object_name = 'obras'
    ordering = ['nome']

class ObraUpdateView(UpdateView):
    model = Obra
    template_name = 'obra_update.html'
    form_class = ObraForm
    success_url = reverse_lazy('obra_list') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Obra atualizada com sucesso!')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class ObraDeleteView(DeleteView):
    model = Obra
    template_name = 'obra_confirm_delete.html'
    success_url = reverse_lazy('obra_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Obra deletada com sucesso!')
        return super().delete(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
#================== Fim das views para obra ==================#

#========================= VIEWS PARA POR ESTADO ========================#
class PorEstadoCreateView(CreateView):
    model = PorEstado
    template_name = 'porestado_create.html'
    form_class = PorEstadoForm
    success_url = reverse_lazy('porestado_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form) 
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class PorEstadoListView(ListView):
    model = PorEstado
    template_name = 'porestado_list.html'
    context_object_name = 'porestados'
    ordering = ['nome']     
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class PorEstadoUpdateView(UpdateView):
    model = PorEstado
    template_name = 'porestado_update.html'
    form_class = PorEstadoForm
    success_url = reverse_lazy('porestado_list') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form) 
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class PorEstadoDeleteView(DeleteView):
    model = PorEstado
    template_name = 'porestado_confirm_delete.html'
    success_url = reverse_lazy('porestado_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
#================== Fim das views para por estado ==========================#   

class ImplantacaoCreateView(CreateView):
    model = Implantacao
    template_name = 'implantacao_create.html'
    form_class = ImplantacaoForm
    success_url = reverse_lazy('implantacao_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)         
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class ImplantacaoListView(ListView):
    model = Implantacao
    template_name = 'implantacao_list.html'
    context_object_name = 'implantacoes'
    ordering = ['nome']     
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class ImplantacaoUpdateView(UpdateView):
    model = Implantacao
    template_name = 'implantacao_update.html'
    form_class = ImplantacaoForm
    success_url = reverse_lazy('implantacao_list') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form) 
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class ImplantacaoDeleteView(DeleteView):
    model = Implantacao
    template_name = 'implantacao_delete.html'
    success_url = reverse_lazy('implantacao_list')  
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
#================== Fim das views para implantação ==========================#      

#========================= VIEWS PARA OBRAS ATIVAS ========================#

class ObrasAtivasCreateView(CreateView):
    model = ObrasAtivas
    template_name = 'obrasativas_create.html'
    form_class = ObrasAtivasForm
    success_url = reverse_lazy('obrasativas_list')  
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class ObrasAtivasListView(ListView):
    model = ObrasAtivas
    template_name = 'obrasativas_list.html'
    context_object_name = 'obrasativas'
    ordering = ['nome']     
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class ObrasAtivasUpdateView(UpdateView):
    model = ObrasAtivas
    template_name = 'obrasativas_update.html'
    form_class = ObrasAtivasForm
    success_url = reverse_lazy('obrasativas_list') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form) 
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class ObrasAtivasDeleteView(DeleteView):
    model = ObrasAtivas
    template_name = 'obrasativas_delete.html'
    success_url = reverse_lazy('obrasativas_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
#================== Fim das views para obras ativas ==========================#   
      
#========================= VIEWS PARA OBRAS DESATIVADAS ========================#
class ObrasDesativadasCreateView(CreateView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_create.html'
    form_class = ObrasDesativadasForm
    success_url = reverse_lazy('obrasdesativadas_list')  

    def form_valid(self, form):
        messages.success(self.request, 'Registro criado com sucesso!')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
class ObrasDesativadasListView(ListView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_list.html'
    context_object_name = 'obrasdesativadas'
    ordering = ['nome']     
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class ObrasDesativadasUpdateView(UpdateView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_update.html'
    form_class = ObrasDesativadasForm
    success_url = reverse_lazy('obrasdesativadas_list') 
    
    def form_valid(self, form):
        messages.success(self.request, 'Registro atualizado com sucesso!')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)

class ObrasDesativadasDeleteView(DeleteView):
    model = ObrasDesativadas
    template_name = 'obrasdesativadas_delete.html'
    success_url = reverse_lazy('obrasdesativadas_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Registro deletado com sucesso!')
        return super().delete(request, *args, **kwargs) 
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('logado'):
            return redirect('usuario_login')
        return super().dispatch(request, *args, **kwargs)
    
#================== Fim das views para obras desativadas ==========================#    
