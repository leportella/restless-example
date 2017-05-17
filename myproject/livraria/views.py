from django.shortcuts import render

from livraria.models import Livro


def LivrosView(request):
    livros = Livro.objects.all()
    context = {'livros': livros}
    return render(request, 'livros.html', context)
