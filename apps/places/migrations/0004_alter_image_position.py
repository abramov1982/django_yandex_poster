# Generated by Django 3.2.9 on 2021-11-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Порядковый номер при отображении'),
        ),
    ]
