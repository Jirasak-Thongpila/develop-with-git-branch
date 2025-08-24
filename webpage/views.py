from django.shortcuts import render

def random_quotes(request):
    return render(request, "random.html")

def index(request):
    return render(request, "index.html")
