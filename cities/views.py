from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from cities.forms import CityForm
from cities.models import City
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

__all__ = (
    'home',
    'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView'
)


def home(request, pk=None):  # функция отображения списка городов
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    #    if pk:
    #        #  city = City.objects.filter(id=pk).first()  # выведит пустую страницу если не существует city
    #        #  city = City.objects.get(id=pk)  # выведет ошибку если не существует city
    #        city = get_object_or_404(City, id=pk)  # вернет ошибку 404
    #        context = {'object': city}
    #        return render(request, 'cities/detail.html', context)

    form = CityForm
    qs = City.objects.all()
    context = {'object_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


# класс отображения детализации городов:
class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


# класс создания нового города:
class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')  # указываем на какую страницу перейти после добавления нового города


# класс редактирования нового города:
class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

#    def get(self, request, *args, **kwargs):
#        return self.post(request, *args, **kwargs)
