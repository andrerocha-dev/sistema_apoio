from django.contrib import admin
from .models import Pessoa, Prestador, Faltas, Atrasos, Ferias, CustoParceiros

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Prestador)
admin.site.register(Faltas)         
admin.site.register(Atrasos)
admin.site.register(Ferias) 
admin.site.register(CustoParceiros)


