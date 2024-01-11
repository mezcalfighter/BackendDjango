from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")