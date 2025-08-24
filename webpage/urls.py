from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random-quotes", views.random_quotes, name="random_quotes"),
]
