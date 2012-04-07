from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __unicode__(self):
        return self.name

