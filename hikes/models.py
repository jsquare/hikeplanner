from django.contrib.gis.db import models

# Create your models here.

class Hike(models.Model):
    name = models.CharField(max_length=100)

    DIFFICULTY_CHOICES = [
        (1, 'easy'),
        (2, 'hard')
    ]
    
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)

    days = models.IntegerField()

    location = models.PointField()

    # Override default manager with GeoManager instance

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

