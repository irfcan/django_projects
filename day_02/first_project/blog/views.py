from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Merhaba Dünya")

# def about(request):
#     return render(request, "about.html")

