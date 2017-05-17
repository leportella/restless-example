from restless.preparers import FieldsPreparer
from restless.dj import DjangoResource

from livraria.models import Autor, Livro


class LivrosResource(DjangoResource):

    preparer = FieldsPreparer(fields={
        'livro_id': 'id',
        'livro_titulo': 'titulo',
        'livro_autor': 'autor.nome',
        'livro_paginas': 'num_paginas',
    })

    def is_authenticated(self):
        return True

    def list(self):
        return Livro.objects.all()

    def detail(self, pk):
        return Livro.objects.get(id=pk)

    def create(self):
        autor = Autor.objects.get(id=self.data.get('autor', ''))
        return Livro.objects.create(
            autor=autor,
            titulo=self.data.get('titulo', ''),
            paginas=self.data.get('paginas', 0),
        )

    def update(self, pk):
        livro = Livro.objects.get(id=pk)
        livro.titulo = self.data.get('titulo', '')
        livro.paginas = self.data.get('paginas', 0)
        livro.save()
        return livro
