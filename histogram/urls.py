from django.urls import path
from histogram import views

urlpatterns = [
    path("", views.home, name="home"),
    path("histogram/<name>", views.hello_there),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]