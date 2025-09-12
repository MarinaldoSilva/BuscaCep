from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=9, primary_key=True)
    logradouro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=150, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    localidade = models.CharField(max_length=150)
    uf = models.CharField(max_length=2)
    regiao = models.CharField(max_length=20)
    ddd = models.IntegerField()

    def __str__(self):
        return f"{self.logradouro}, {self.bairro} - {self.localidade}/{self.uf}"



