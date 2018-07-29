from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100,null=False)
    email = models.CharField(max_length=150,null=False)
    senha = models.CharField(max_length=50,null=False)
    endereco = models.TextField(null=False)

    def __str__(self):
        return self.nome
