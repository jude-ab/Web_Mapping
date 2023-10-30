from django.contrib.gis import admin
from .models import StoneCircle, UserProfile
# Register your models here.

admin.site.register(StoneCircle, admin.OSMGeoAdmin)
admin.site.register(UserProfile, admin.OSMGeoAdmin)