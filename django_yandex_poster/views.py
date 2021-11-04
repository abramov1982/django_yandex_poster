from django.shortcuts import render

from apps.places.models import PlaceCoord

from apps.places.utils import make_geojson


def index(request):
    places = make_geojson()
    context = {'places': places}
    return render(request, 'index.html', context)
