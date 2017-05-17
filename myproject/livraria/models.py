from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=250)


class Livro(models.Model):
    autor = models.ForeignKey('Autor')
    titulo = models.CharField(max_length=250)
    paginas = models.PositiveIntegerField()

    @property
    def num_paginas(self):
        return '{} paginas'.format(self.paginas)
