from django.http import HttpResponse
from django.template import Context,Template,loader
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")