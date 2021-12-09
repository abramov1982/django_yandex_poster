import collections

from .models import Place


def get_places(places_pk):
    if places_pk:
        places = Place.objects.filter(pk__in=places_pk)
    else:
        places = Place.objects.all()
    return places


def place_detail(place):
    detail = {"type": "Feature",
              "geometry": {
                  "type": "Point",
                  "coordinates": [place.longitude, place.latitude]
              },
              "properties": {
                  "title": place.title,
                  "detailsUrl": f'places/{place.pk}'
              }
              }
    return detail


def make_geojson(places_pk=None):
    geojson = {"type": "FeatureCollection", "features": []}
    places = get_places(places_pk)
    for place in places:
        geojson["features"].append(place_detail(place))
    return geojson
