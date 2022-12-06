from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def appp(request):
    json = {"Message": "Hello World!"}
    return JsonResponse(json)