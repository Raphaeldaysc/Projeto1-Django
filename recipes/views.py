from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={'name': 'Raphael Dias Câmara'})


def contato(request):
    return HttpResponse("""Raphael Dias Camara <br/>
                        Contato: 84-994986498""")
