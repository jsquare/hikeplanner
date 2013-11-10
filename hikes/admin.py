from django.contrib.gis import admin
from models import Hike

admin.site.register(Hike, admin.OSMGeoAdmin)