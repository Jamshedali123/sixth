from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jspider(request):
    return HttpResponse('java full stack developer app_string')

def pyspider(request):
    return HttpResponse('python full stack developer app1_string')
