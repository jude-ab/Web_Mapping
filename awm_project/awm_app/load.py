from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import StoneCircle

stone_circles = {
    'county' : 'COUNTY',
    'lon' : 'LONGITUDE',
    'lat' : 'LATITUDE',
    'mpoly' : 'POINT',
}

stone_circles_shp = Path(__file__).resolve().parent / 'data' / 'StoneCircles-point.shp'

def run(verbose=True):
    lm = LayerMapping(StoneCircle, stone_circles_shp, stone_circles, transform=False)
    lm.save(strict=True, verbose=verbose)
