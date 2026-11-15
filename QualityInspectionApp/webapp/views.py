from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"webapp/home.html")

def register(request):
    return render(request,"webapp/register.html")

def welcome(request):
    return render(request,"webapp/welcomepage.html")

def inspectionlist(request):
    return render(request, "webapp/qualityinspection.html")

def records(request):
    return render(request, "webapp/inspection_records.html")

def analytics(request):
    return render(request, "webapp/inspection_analytics.html")

def regulations(request):
    return render(request, "webapp/qualityRegulations.html")

def f2(request):
    return render(request, "webapp/F2.html")
