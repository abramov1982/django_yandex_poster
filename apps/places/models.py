from django.db import models

from tinymce.models import HTMLField

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(blank=True, verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        app_label = 'places'
        db_table = 'places'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', verbose_name='Изображение места')
    image = models.ImageField(upload_to='places/images', verbose_name='Изображение')
    position = models.PositiveIntegerField(default=0, null=False,
                                           verbose_name='Порядковый номер при отображении')

    def __str__(self):
        return self.place.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        app_label = 'places'
        db_table = 'images'
        ordering = ['position']
