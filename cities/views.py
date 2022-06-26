from django.shortcuts import render

# функция отображения списка городов:
from cities.models import City


__all__ = (
    'home',
)

def home(request):
    qs = City.objects.all()
    context = {'object_list': qs}
    return render(request, 'cities/home.html', context)
