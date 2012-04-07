from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from wkhtmltopdf.views import PDFTemplateView

from cache.views import CacheView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cache/', CacheView.as_view(), name='cache'),
    url(r'^pdf/$', PDFTemplateView.as_view(filename='my_pdf.pdf', template_name='pdf.html'), name='pdf'),

    url(r'', include('prototype.auth_urls')),
)

