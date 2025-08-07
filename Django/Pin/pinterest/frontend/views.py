from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "frontend/home.html")

def create(request):
    return render(request, "frontend/create.html")

def view(request):
    return render(request, "frontend/pin.html")