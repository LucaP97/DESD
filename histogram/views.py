from django.shortcuts import render
from django.http import HttpResponse
from histogram import createHistogram
import datetime


# def home(request):
#     #return HttpResponse("Hello, Django")
#     return HttpResponse(createHistogram.runHistogram())

def home(request):
    return render(request, "histogram/home.html")

def about(request):
    return render(request, "histogram/about.html")

def contact(request):
    return render(request, "histogram/contact.html")

# Create your views here.

def hello_there(request, name):
    return render(
        request,
        'histogram/histogram_there.html',
        {
            'name': name,
            'date': datetime.datetime.now()
        }
    )



# def hello_there(request):
#     context = {'Luca': 'date'}
#     return render(
#         request,
#         'histogram/histogram_there.html',
#         context
#     )