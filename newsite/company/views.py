from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("привет чувак")

def categories(request, catid):
    return HttpResponse(f"<h1>Кампании по категориям</h1><p>{catid}</p>")

