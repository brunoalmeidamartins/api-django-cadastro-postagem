from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    url_imagem = models.URLField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.titulo
