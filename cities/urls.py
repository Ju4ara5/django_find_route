from django.urls import path

from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),  # к имени класса добавляем as_view для отображения
    path('add/', CityCreateView.as_view(), name='create'),
]
