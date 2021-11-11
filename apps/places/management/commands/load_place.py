import requests
from PIL import Image as IMG
from io import BytesIO

from django.core.management.base import BaseCommand
from apps.places.models import Place, Image


class Command(BaseCommand):
    help = 'Load Places from GitHub to DB'

    def handle(self, *args, **options):
        print('Load Places and Images complete')

    with requests.Session() as session:
        files_raw = []
        repo_url = 'https://api.github.com/repos/devmanorg/where-to-go-places/git/trees/master?recursive=1'
        raw_url = 'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/'
        request_repo_list = session.get(repo_url)
        repo_list = request_repo_list.json()
        for file in repo_list['tree']:
            if file['path'][-4:] == 'json':
                request_raw = session.get(raw_url + file['path'])
                raw = request_raw.json()
                files_raw.append(raw)
                place, created = Place.objects.get_or_create(
                    title=raw['title'],
                    description_long=raw['description_long'],
                    description_short=raw['description_short'],
                    latitude=raw['coordinates']['lat'],
                    longitude=raw['coordinates']['lng'],
                )
                place.save()
                print(f'{place.title} was save')
                for image_url in raw['imgs']:
                    image_data = IMG.open(BytesIO(requests.get(image_url).content))
                    image_name = image_url.split('/')[-1]
                    image_data.save(f'./media/places/images/{image_name}')
                    image, created = Image.objects.get_or_create(place=Place.objects.get(pk=place.pk),
                                                                 image=f'places/images/{image_name}')
                    image.save()
                    print(f'Image {image_name} for {place.title} was save')

