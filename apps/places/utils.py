from .models import PlaceCoord


def make_geojson():
    geojson = {"type": "FeatureCollection", "features": []}
    places = PlaceCoord.objects.all()
    for place in places:
        place_dict = {"type": "Feature",
                      "geometry": {
                          "type": "Point",
                          "coordinates": [place.latitude, place.longitude]
                        },
                      "properties": {
                          "title": place.title,
                          "placeId": place.placeId,
                          "detailsUrl": place.detailsUrl
                        }
                      }
        geojson["features"].append(place_dict)
    return geojson
