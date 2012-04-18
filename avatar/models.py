from django.contrib import admin
from django.db import models


class Avatar(models.Model):
    img = models.ImageField(upload_to='uploads')


admin.site.register(Avatar)
