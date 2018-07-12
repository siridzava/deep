from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'dive_in/index.html')


def initiative(request):
    return render(request, 'dive_in/initiative.html')
