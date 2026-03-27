from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Obra(Base):
    nome = models.CharField('Nome da Obra', max_length=100)
    construtora = models.CharField('Construtora', max_length=100)
    
    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'

    def __str__(self):
        return self.nome
    
class PorEstado(Base):
    MODELO_CHOICES = [
        ('digicon/controlid', 'Digicon/Controlid'),
        ('controlid', 'Controlid'),
        ('digicon', 'Digicon'),
    ]
    
    nome = models.ForeignKey("Obra", verbose_name=_("Nome da Obra"), on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=100, choices=MODELO_CHOICES, default='Selecione o modelo')
    ticket = models.CharField('Ticket', max_length=100)
    base = models.BooleanField(_("Base"), default=False)
    facial = models.BooleanField(_("Facial"), default=False)
    webcam = models.BooleanField(_("Webcam"), default=False)
    ativacao = models.DateField(_("Data da Ativação"), null=True, blank=True)
    nfe = models.IntegerField(_("Nota Fiscal"), null=True, blank=True)
    
    class Meta:
        verbose_name = 'Por Estado'
        verbose_name_plural = 'Por Estados'
    
    def __str__(self):
        return self.nome
    
class Implantacao(Base):
    # Definindo as opções (Choices)
    STATUS_CHOICES = [
        ('equipamento_entregue', 'Equipamento Entregue'),
        ('aguardando_cliente', 'Aguardando Cliente'),
        ('pendente_fechamento', 'Pendente Fechamento'),
        ('envio_autorizado', 'Envio Autorizado'),
        ('aguardando_aprovacao', 'Aguardando Aprovação'),
    ]
    
    MODELO_CHOICES = [
        ('digicon/controlid', 'Digicon/Controlid'),
        ('controlid', 'Controlid'),
        ('digicon', 'Digicon'),
    ]

    nome = models.ForeignKey("Obra", verbose_name=_("Nome da Obra"), on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=100, choices=MODELO_CHOICES, default='Selecione o modelo')	
    status = models.CharField('Status',max_length=100,choices=STATUS_CHOICES,default='Selecione o status',)
    ticket = models.CharField('Ticket', max_length=100)
    base = models.BooleanField(_("Base"), default=False)
    webcam = models.BooleanField(_("Webcam"), default=False)
    ativacao = models.DateField(_("Data da Ativação"), null=True, blank=True)
    nfe = models.IntegerField(_("Nota Fiscal"), null=True, blank=True)
    informacao = models.TextField(_("Informações Adicionais"), null=True, blank=True)

    class Meta:
        verbose_name = 'Implantação'
        verbose_name_plural = 'Implantações'

    def __str__(self):        
        return self.nome 
    
    
class ObrasAtivas(Base):
    # Definindo as opções (Choices)
    MODELO_CHOICES = [
        ('digicon/controlid', 'Digicon/Controlid'),
        ('controlid', 'Controlid'),
        ('digicon', 'Digicon'),
    ]
     
    nome = models.ForeignKey("Obra", related_name="ativas_nome", on_delete=models.CASCADE)
    construtora = models.ForeignKey("Obra", related_name="ativas_construtora", on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=100, choices=MODELO_CHOICES, default='Selecione o modelo')
    

    class Meta:
        verbose_name = 'Obra Ativa'
        verbose_name_plural = 'Obras Ativas'

    def __str__(self):
        return self.nome
    
    
class ObrasDesativadas(models.Model):
    nome = models.ForeignKey("Obra", related_name="desativadas_nome", on_delete=models.CASCADE)
    construtora = models.ForeignKey("Obra", related_name="desativadas_construtora", on_delete=models.CASCADE)
    desativacao = models.DateField(_("Data da Desativação"), null=True, blank=True)

    class Meta:
        verbose_name = 'Obra Desativada'
        verbose_name_plural = 'Obras Desativadas'

    def __str__(self):
        return self.nome   
    
    
    