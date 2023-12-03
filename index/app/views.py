from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'one.html')


def info(request):
    return render(request, 'two.html')


def read(request):
    return render(request, 'three.html')


def registration(request):
    return render(request, 'registration.html')