from django.http import HttpResponse
from django.shortcuts import render

# Methode View
def index(request) : 
    return render(request, 'index.html')

def about(request):
    return render(request, "about.html")

