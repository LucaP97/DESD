from django.urls import path
from histogram import views

urlpatterns = [
    path("", views.home, name="home"),
]