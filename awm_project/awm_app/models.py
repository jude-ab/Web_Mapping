from django.contrib.gis.db import models
from django.contrib.auth.models import User

class StoneCircle(models.Model):
    county = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    mpoly = models.PointField(srid=4326)

    def __str__(self):
        return self.county

# Extending in-built user model with one-to-one relationship
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50, null=True)
    