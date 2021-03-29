# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template


def home(request):
    return render(request, 'templates/static_handler.html')

# def home(request):
#    return HttpResponse("Привет, мир!", content_type="text/plain; charset=utf-8")
