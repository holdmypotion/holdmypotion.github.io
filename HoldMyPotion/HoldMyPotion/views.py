from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    """Returns the home page"""
    return render(request, 'home.html')

def about_page(request):
    """Returns the about page"""
    return render(request, 'about.html')
