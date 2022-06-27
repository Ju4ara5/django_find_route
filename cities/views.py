from django.shortcuts import render, get_object_or_404

# функция отображения списка городов:
from cities.models import City


__all__ = (
    'home',
)


def home(request, pk=None):
    if pk:
        #  city = City.objects.filter(id=pk).first()  # выведит пустую страницу если не существует city
        #  city = City.objects.get(id=pk)  # выведет ошибку если не существует city
        city = get_object_or_404(City, id=pk)  # вернет ошибку 404
        context = {'object': city}
        return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'object_list': qs}
    return render(request, 'cities/home.html', context)
