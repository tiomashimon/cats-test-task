from django.shortcuts import render

def signup(request):
    return render(request, 'client/signup.html')

def signin(request):
    return render(request, 'client/signin.html')

def home(request):
    return render(request, 'client/home.html')

def profile(request):
    return render(request, 'client/profile.html')

def about(request):
    return render(request, 'client/about.html')

def verification(request):
    return render(request, 'client/verification.html')