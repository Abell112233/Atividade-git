from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Abell1(request):
    return render(request, "Abell1/Abell1.html")

def index(request):
    return render(request, "Abell1/index.html")