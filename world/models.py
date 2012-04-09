from django.contrib.gis import admin
from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    point = models.PointField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    @property
    def x(self):
        return self.point.x

    @property
    def y(self):
        return self.point.y


admin.site.register(Place)#, admin.GeoModelAdmin)

