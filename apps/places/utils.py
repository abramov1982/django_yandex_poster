from .models import Place


def make_geojson():
    geojson = {"type": "FeatureCollection", "features": []}
    places = Place.objects.all()
    for place in places:
        place_dict = {"type": "Feature",
                      "geometry": {
                          "type": "Point",
                          "coordinates": [place.longitude, place.latitude]
                        },
                      "properties": {
                          "title": place.title,
                          "detailsUrl": f'places/{place.pk}'
                        }
                      }
        geojson["features"].append(place_dict)
    return geojson
