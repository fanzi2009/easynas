from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView

urlpatterns = patterns('',
    url(r'^pool_status$', 'storage.views.pool_status'),
    url(r'^get_disks$', 'storage.views.get_disks')
)
