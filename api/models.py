from django.db import models


# Create your models here.

class Produto(models.Model):
    descricao = models.CharField(max_length=12)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao
