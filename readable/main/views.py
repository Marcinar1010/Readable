from django.shortcuts import render
from django.http import HttpResponse

# home page
def home(request):
    return render(request, 'main/home.html')

# about the project page
def about(request):
    return render(request, 'main/about.html')
