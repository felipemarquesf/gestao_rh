from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresas

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100 , help_text= 'Nome do funcionario')
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresas,on_delete=models.PROTECT)
def __str__(self):
    return self.nome
