from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'company/index.html')


def about(request):
    return render(request, 'company/about.html')


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Кампании по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False) #без permanent будет статус 302, то есть временный. А так 301  #raise Http404() - можно и так оставить.
    return HttpResponse(f"<h1>Кампании по годам</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
