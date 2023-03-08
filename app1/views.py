from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Mahesh(request):
    return HttpResponse("<h1 style='color:blue;'>My name is Mahesh</h1>")
def Afrin(request):
    return HttpResponse("<h1 style='color:red;'>My name is Afrin</h1>")