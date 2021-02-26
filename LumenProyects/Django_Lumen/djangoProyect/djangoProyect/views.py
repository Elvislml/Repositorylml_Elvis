from django.shortcuts import render

def index(request):
    return render(render, 'homepage.html')