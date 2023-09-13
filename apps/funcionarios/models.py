from django.db import models

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100 , help_text= 'Nome do funcionario')

def __str__(self):
    return self.nome
