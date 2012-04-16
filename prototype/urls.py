from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from wkhtmltopdf.views import PDFTemplateView

from cache.views import CacheView
from world.views import PlaceView


admin.autodiscover()


class ExceptionView(TemplateView):
    def get_context_data(self, **kwargs):
        1/0
        return super(ExceptionView, self).get_context_data(**kwargs)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cache/', CacheView.as_view(), name='cache'),
    url(r'^exception', ExceptionView.as_view(), name='exception'),
    url(r'^geo/', PlaceView.as_view(), name='geo'),
    url(r'^pdf/$', PDFTemplateView.as_view(filename='my_pdf.pdf', template_name='pdf.html'), name='pdf'),

    url(r'', include('prototype.auth_urls')),
)

