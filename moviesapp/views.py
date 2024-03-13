from django.shortcuts import render
from django.http import HttpResponse


def movies_list(request):
    return HttpResponse("Movie Database Application")
