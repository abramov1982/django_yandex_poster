from django.db import models


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
    number = models.PositiveSmallIntegerField(blank=False, verbose_name='Порядковый номер при отображении')

    def __str__(self):
        return self.place.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        unique_together = ('place', 'number',)
        app_label = 'places'
        db_table = 'images'


class PlaceCoord(models.Model):
    latitude = models.FloatField(blank=False, null=True, verbose_name='Широта')
    longitude = models.FloatField(blank=False, null=True, verbose_name='Долгота')
    title = models.CharField(max_length=200, unique=True, blank=False, verbose_name='Описание')
    placeId = models.CharField(max_length=200, unique=True, blank=False, verbose_name='ID места')
    detailsUrl = models.URLField(blank=False, verbose_name='URL детального описания места')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Координаты места'
        verbose_name_plural = 'Координаты мест'
        app_label = 'places'
        db_table = 'place_coord'
