from django.http import HttpResponse
from django.shortcuts import render

def Saludo(request):
    return HttpResponse("Hola mundo")

def index(request):
    return render(request,'index.html')

def nintendo(request):
    return render(request,'nintendo.html')

def pc(request):
    return render(request,'PC.html')

def play(request):
    return render(request,'Play_Station.html')

def xbox(request):
    return render(request,'Xbox.html')

def login(request):
    return render(request,'login.html')