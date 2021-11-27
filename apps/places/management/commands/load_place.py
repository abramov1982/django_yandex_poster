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
        place_files = requests.get(repo_url)
        if not place_files.status_code == 200:
            return "Can't get files"
        files_serialize = place_files.json()
        for file in files_serialize['tree']:
            filename = urlparse(unquote(file['path'])).path
            if not filename[-4:] == 'json':
                continue
            place_raw = requests.get(raw_url + file['path'])
            if not place_raw.status_code == 200:
                print("Can't load json file")
                continue
            place_serialize = place_raw.json()
            place, created = Place.objects.get_or_create(
                title__iexact=place_serialize['title'],
                latitude=place_serialize['coordinates']['lat'],
                longitude=place_serialize['coordinates']['lng'],
                defaults={'title': place_serialize['title'],
                          'description_long': place_serialize['description_long'],
                          'description_short': place_serialize['description_short'],
                          'latitude': place_serialize['coordinates']['lat'],
                          'longitude': place_serialize['coordinates']['lng'],
                          }
            )
            place.save()
            print(f'{place_serialize["title"]} was save')
            for image_url in place_serialize['imgs']:
                if not requests.get(image_url).status_code == 200:
                    print(f"Can't load image by {image_url} url")
                    continue
                image_data = IMG.open(BytesIO(requests.get(image_url).content))
                image_name = urlparse(unquote(image_url)).path.split('/')[-1]
                image_data.save(f'./media/places/images/{image_name}')
                image, created = Image.objects.get_or_create(place=Place.objects.get(pk=place.pk),
                                                             image=f'places/images/{image_name}')
                image.save()
                print(f'Image {image_name} for {place.title} was save')
        print('Load Places and Images complete')
