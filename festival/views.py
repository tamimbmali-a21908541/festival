from django.shortcuts import render, get_object_or_404
from .models import Banda, Palco, Dia, Concerto


def index_view(request):
    return render(request, 'festival/index.html')


def dias_view(request):
    dias = Dia.objects.all()

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)


def palcos_view(request):
    palcos = Palco.objects.all()

    context = {'palcos': palcos}

    return render(request, 'festival/palcos.html', context)


def concerto_view(request, id):
    concerto = get_object_or_404(Concerto, id=id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)
