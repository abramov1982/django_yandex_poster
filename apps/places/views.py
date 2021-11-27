from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404


from apps.places.models import Place, Image

from apps.places.utils import make_geojson


def index(request):
    places = make_geojson()
    context = {'places': places}
    return render(request, 'index.html', context)


def place_by_id(request, pk):
    place = get_object_or_404(Place, pk=pk)
    images = [place.image.url for place in place.images.all()]
    place_info = {'title': place.title,
                  'imgs': images,
                  'description_short': place.description_short,
                  'description_long': place.description_long,
                  'coordinates': {'lat': place.latitude, 'lng': place.longitude}
                  }
    return JsonResponse(place_info, json_dumps_params={'ensure_ascii': False, 'indent': 2})

