# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.context_processors import csrf

from django.http import QueryDict

from middleware.text2html import *
from middleware.marvin_nas import *

from easynas.models import ZPool
from easynas.serializers import ZPoolSerializer

from rest_framework import generics

import logging

logger = logging.getLogger('easynas.web')


def create_zpool(request):

    logger.info('create_zpool')

    context = {}
    context.update(csrf(request))

    disks = [
        {"name":"ad1","capacity":100},
        {"name":"ad3","capacity":400},
        {"name":"ad4","capacity":200},
        ]
    context["disks"] = disks

    return render_to_response('storage/dialog/create_zpool.html',context)


def list_zpool(request):

    logger.info('list_zpool')

    return render_to_response('storage/dialog/list_zpool.html',context)
    