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
        db_table = 'place'
