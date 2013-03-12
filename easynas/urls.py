from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from easynas.views import *

urlpatterns = patterns('',
    url(r'^pool_status$', 'easynas.views.pool_status'),
    url(r'^get_disks$', 'easynas.views.get_disks'),
    url(r'^zpools$', ZPoolList.as_view()),
    url(r'^zpools/(?P<pk>[0-9]+)/$', ZPoolDetail.as_view(), name='zpools-detail'),
    url(r'^test2$', 'easynas.views.test2'),
    url(r'^test$', 'easynas.views.test'),
    url(r'^storage/dialog/create_zpool$', 'easynas.storage_dialog.create_zpool'),
    url(r'^storage/dialog/list_zpool$', 'easynas.storage_dialog.list_zpool')
)
