from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        pass
