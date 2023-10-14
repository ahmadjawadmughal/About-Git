# from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.

def update(request):

    Note.objects.filter(Name=XYZ).update(Name=ABC)
    Note.save()