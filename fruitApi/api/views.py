from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
  return HttpResponse("<h2>This API is working<h3>");