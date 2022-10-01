from django.db import models
from datetime import datetime

class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100)
    video = models.CharField(max_length=82)
    modo_preparo = models.TextField()
    ingredientes = models.TextField()
    nota = models.TextField()
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
    
