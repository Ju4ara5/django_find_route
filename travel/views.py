from django.shortcuts import render


def home(request):
    name = 'Bob'
    return render(request, 'cities.html', {'name': name})


def about(request):
    name = 'About as'
    return render(request, 'about.html', {'name': name})
