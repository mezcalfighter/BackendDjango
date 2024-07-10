from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("You are in about section")