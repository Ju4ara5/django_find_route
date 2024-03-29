from django.db import models
from django.urls import reverse


# класс который будет работать с базой данных через ORM


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']  # сортируем базу данных таблицы в алфавитном порядке

    # Сюда (на детализацию записи) переходим после нажатия кнопки 'Сохранить'(новый город):
    # Это по умолчанию, если не указать во views / class CityCreateView(CreateView) / success_url...
    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})
