# frontend/views.py
from django.shortcuts import render

def blog(request):
    return render(request, 'frontend/blog.html')
