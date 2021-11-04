from django.db import models

from django_yandex_poster.settings import MEDIA_ROOT


# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name='Название')
    description_short = models.TextField(blank=False, verbose_name='Краткое описание')
    description_long = models.TextField(blank=False, verbose_name='Полное описание')
    coordinates = models.JSONField(blank=False, verbose_name='координаты места')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        app_label = 'places'
        db_table = 'places'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='image', verbose_name='Изображение места')
    image = models.ImageField(upload_to='places/images', verbose_name='Изображение')

    def __str__(self):
        return self.place.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        app_label = 'places'
        db_table = 'images'
