from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<H2>HEY! Welcome TVS</H2")