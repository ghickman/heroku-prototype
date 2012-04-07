from django.core.cache import cache
from django.views.generic import DetailView

from .models import Item


class CacheView(DetailView):
    def get_object(self):
        cached_item = cache.get('item')
        if cached_item:
            return cached_item

        try:
            item = Item.objects.get(pk=1)
        except Item.DoesNotExist:
            item = Item.objects.create(name='Herp Derp', body='Herp Derpin all over the USA')
        else:
            cache.set('item', item, 300)
            return item

