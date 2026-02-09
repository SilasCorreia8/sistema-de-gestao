from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.CharField(max_length=180)
    quantidade = models.PositiveIntegerField()
    validade = models.DateField()

    def __str__(self):
        return self.nome