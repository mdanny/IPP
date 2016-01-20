# from django.conf.urls import patterns, url;

# from beers import views;

# urlpatterns = patterns('',
#     url(r'^$', views.index, name='index')
# );

from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BeerList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BeerDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)


