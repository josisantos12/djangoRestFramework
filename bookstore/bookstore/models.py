from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publicado_em = models.DateField()

    def __str__(self):
        return f"{self.titulo} por {self.autor}"