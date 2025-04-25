
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome




class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_agendada = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.servico.nome} em {self.data_agendada}"
