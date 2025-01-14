from django.urls import path
from TaskManager import views


urlpatterns = [
    path("", views.index),
]
