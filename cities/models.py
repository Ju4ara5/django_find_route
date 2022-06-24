from django.db import models

# класс который будет работать с базой данных через ORM


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']  # сортируем базу данных таблицы в алфавитном порядке
