from django.shortcuts import render
from django.http import HttpResponse
from histogram import createHistogram


def home(request):
    #return HttpResponse("Hello, Django")
    return HttpResponse(createHistogram.runHistogram())

# Create your views here.
