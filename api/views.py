from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showMessage(request):
    return HttpResponse('Hello World')