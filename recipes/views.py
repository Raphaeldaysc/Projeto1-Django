from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Ola Home</h1>")


def contato(request):
    return HttpResponse("""Raphael Dias Camara <br/>
                        Contato: 84-994986498""")
