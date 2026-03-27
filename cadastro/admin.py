from django.contrib import admin

from obra.models import Implantacao, Obra, PorEstado, ObrasAtivas, ObrasDesativadas
from .models import Pessoa, Prestador, Faltas, Atrasos, Ferias, CustoParceiros
# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Prestador)
admin.site.register(Faltas)         
admin.site.register(Atrasos)
admin.site.register(Ferias) 
admin.site.register(CustoParceiros)
admin.site.register(Obra)
admin.site.register(PorEstado)
admin.site.register(Implantacao) 
admin.site.register(ObrasAtivas)
admin.site.register(ObrasDesativadas)


