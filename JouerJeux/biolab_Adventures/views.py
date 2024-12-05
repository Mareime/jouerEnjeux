from django.shortcuts import render
from django.http import HttpResponse
# from django
# Create your views here.
def Home():
    return HttpResponse("Hello, world. You're at the polls index.")

    