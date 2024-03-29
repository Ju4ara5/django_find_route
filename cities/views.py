from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from cities.forms import CityForm
from cities.models import City
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

__all__ = (
    'home',
    'CityDetailView', 'CityCreateView', 'CityUpdateView', 'CityDeleteView', 'CityListView'
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
    lst = Paginator(qs, 2)  # 2 записи на 1 странице
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


# класс отображения детализации городов:
class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


# класс создания нового города:
class CityCreateView(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')  # указываем на какую страницу перейти после добавления нового города
    success_message = "Город успешно создан"


# класс редактирования нового города:
class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно отредактирован."


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город будет удалён.')
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 2  # 2 записи на 1 странице
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm
        context['form'] = form
        return context

