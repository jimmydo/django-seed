from django.conf.urls.defaults import *

urlpatterns = patterns('seed.views',
    url(r'^$', 'index'),
)
