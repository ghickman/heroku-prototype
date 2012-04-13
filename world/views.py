from django.views.generic import DetailView

from .models import Place


class PlaceView(DetailView):
    model = Place

    def get_context_data(self, **kwargs):
        1/0
        return {'lat': self.object.x, 'lng': self.object.y}

    def get_object(self):
        try:
            place = self.model.objects.get(pk=1)
        except self.model.DoesNotExist:
            place = self.model.objects.create()
        finally:
            return place

