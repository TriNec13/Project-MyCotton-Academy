from django.shortcuts import render

# Create your views here.
def front(request):
    return render(request, 'Blog.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')