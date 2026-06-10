from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def ideas(request):
    return render(request, 'ideas.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')
