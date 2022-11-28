from django.urls import path
from histogram import views
from histogram.models import logMessage

home_list_view = views.HomeListView.as_view(
    queryset=logMessage.objects.order_by("-log_date")[:5], # [:5] limits the results to the 5 most recent
    context_object_name = "message_list",
    template_name = "histogram/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("histogram/<name>", views.hello_there),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]

