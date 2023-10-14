from django.urls import path

from notesapp.views import *

urlpatterns = [
    path("update/", update, name="update"),
]