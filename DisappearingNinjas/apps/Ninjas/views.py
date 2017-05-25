from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'Ninjas/index.html')


def ninja(request):
    context = {
        'color': ""
    }
    return render(request, 'Ninjas/ninja.html', context)


def ninja_color(request, color):
    context = {
        'color': color
    }
    return render(request, 'Ninjas/ninja.html', context)
