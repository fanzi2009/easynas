from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^test1$', 'mydata.views.test1'),
    url(r'^test2$', 'mydata.views.test2')
)
