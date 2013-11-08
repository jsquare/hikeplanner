from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

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

    def get_absolute_url(self):
        slug = slugify(self.name)
        url = reverse('hike-detail', kwargs={'hike_id': self.id, 'slug': slug})
        return url

    def __unicode__(self):
        return self.name
