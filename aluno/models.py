from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def _str_(self):
        return self.nome
