from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')
def Abell1(request):
    return render (request, "my_app/abell1.html")
def Abell2(request):
    return render (request, "my_app/abell2.html")
