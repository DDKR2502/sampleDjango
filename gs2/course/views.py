from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_jango(request):
    return HttpResponse('Hello Django')
def learn_py(request):
    return HttpResponse('Hello python')
