from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_admissao = models.DateField(
        'Data de Admissão', null=True, blank=True)
    funcao = models.CharField('Função', max_length=100, null=True, blank=True)
    endereco = models.CharField(
        'Endereço', max_length=255, null=True, blank=True)
    documento = models.CharField(
        'Documento', max_length=50, null=True, blank=True)
    prestador = models.ForeignKey(
        'Prestador', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


class Prestador(models.Model):
    nome = models.CharField('', max_length=50)

    def __str__(self):
        return self.nome


class Faltas(models.Model):
    nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_falta = models.DateField('Data da Falta')
    justificada = models.BooleanField('Justificada', default=False)

    def __str__(self):
        return f'{self.nome.nome} - {self.data_falta}'


class Atrasos(models.Model):
    nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_atraso = models.DateField('Data do Atraso')
    horario = models.TimeField('Horário do Atraso', null=True, blank=True)
    justificado = models.BooleanField('Justificado', default=False)

    def __str__(self):
        return f'{self.nome.nome} - {self.data_atraso}'


class Ferias(models.Model):
    nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_admissao = models.DateField('Data de Admissão', null=True, blank=True)
    data_limite = models.DateField('Vencimento das Férias', null=True, blank=True)
    periodo_aquisitivo = models.DateField('Início Aquisitivo', null=True, blank=True)
    fim_aquisitivo = models.DateField('Fim Aquisitivo', null=True, blank=True)
    limite_gozo = models.DateField('Limite para Gozo', null=True, blank=True)
    inicio_gozo = models.DateField('Início do Gozo', null=True, blank=True)
    fim_gozo = models.DateField('Fim do Gozo', null=True, blank=True)

    def __str__(self):
        return f'{self.nome.nome} - {self.data_admissao} a {self.data_limite}'


class CustoParceiros(models.Model):
    nome = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    hora_tecnica = models.DecimalField(
        'Valor Hora Técnica', max_digits=10, decimal_places=2)
    hora_adcional = models.DecimalField(
        'Valor por Hora Adicional', max_digits=10, decimal_places=2)
    remanejamento = models.DecimalField(
        'Valor Remanejamento', max_digits=10, decimal_places=2)
    instalacao_1_catraca = models.DecimalField(
        'Valor Instalação de 01 Catraca', max_digits=10, decimal_places=2)
    instalacao_2_catracas = models.DecimalField(
        'Valor Instalação de 02 Catracas', max_digits=10, decimal_places=2)
    desmobilizacao = models.DecimalField(
        'Valor Desmobilização', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome.nome} - R${self.hora_tecnica}'
