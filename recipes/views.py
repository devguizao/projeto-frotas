from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home 2')

def contato(request):
    return HttpResponse('meu contato')

def sobre(request):
    return HttpResponse('sobre mim')
