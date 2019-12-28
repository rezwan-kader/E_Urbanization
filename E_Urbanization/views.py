from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def home_2(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')


def single_blog(request):
    return render(request, 'single-blog.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def appointments(request):
    return render(request, 'appointments.html')


def blog(request):
    return render(request,'blog.html')