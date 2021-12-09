import os
import posixpath

import requests

from io import BytesIO
from PIL import Image as IMG
from urllib.parse import urlparse, unquote

from django.core.management.base import BaseCommand
from apps.places.models import Place, Image


class Command(BaseCommand):
    help = 'Load Places from GitHub to DB'

    def handle(self, *args, **options):
        repo_url = 'https://api.github.com/repos/devmanorg/where-to-go-places/git/trees/master?recursive=1'
        raw_url = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/'
        place_files_response = requests.get(repo_url)
        place_files_response.raise_for_status()
        serialized_files = place_files_response.json()
        for file in serialized_files['tree']:
            filename = urlparse(unquote(file['path'])).path
            if not os.path.splitext(filename)[1] == '.json':
                continue
            place_raw_response = requests.get(raw_url + file['path'])
            place_raw_response.raise_for_status()
            place_serialized = place_raw_response.json()
            place, created = Place.objects.get_or_create(
                title__iexact=place_serialized['title'],
                latitude=place_serialized['coordinates']['lat'],
                longitude=place_serialized['coordinates']['lng'],
                defaults={'title': place_serialized['title'],
                          'description_long': place_serialized['description_long'],
                          'description_short': place_serialized['description_short'],
                          'latitude': place_serialized['coordinates']['lat'],
                          'longitude': place_serialized['coordinates']['lng'],
                          }
            )
            print(f'{place_serialized["title"]} was save')
            for image_url in place_serialized['imgs']:
                image_response = requests.get(image_url)
                image_response.raise_for_status()
                image_data = IMG.open(BytesIO(image_response.content))
                image_name = urlparse(unquote(image_url)).path.split('/')[-1]
                image_data.save(f'./media/places/images/{image_name}')
                image, created = Image.objects.get_or_create(place=Place.objects.get(pk=place.pk),
                                                             image=f'places/images/{image_name}')
                print(f'Image {image_name} for {place.title} was saved')
        print('Load Places and Images complete')
