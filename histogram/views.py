from django.shortcuts import render
from django.http import HttpResponse
from histogram import createHistogram
import datetime
from django.shortcuts import redirect
from histogram.forms import logMessageForm
from histogram.models import logMessage
from django.views.generic import ListView


# def home(request):
#     #return HttpResponse("Hello, Django")
#     return HttpResponse(createHistogram.runHistogram())

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = logMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

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

def log_message(request):
    form = logMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "histogram/log_message.html", {"form": form})


# def hello_there(request):
#     context = {'Luca': 'date'}
#     return render(
#         request,
#         'histogram/histogram_there.html',
#         context
#     )