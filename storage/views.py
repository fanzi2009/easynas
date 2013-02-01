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

from storage.models import ZPool

import logging

logger = logging.getLogger('easynas.web')

#http://192.168.80.128:8080/storage/pool_status
#http://192.168.80.128:8080/storage/get_disks

def get_disks(request):
    result = 'No, Type, Size\n'

    #disks = notifier().get_disks()
    # disks = {
    #     "ad1":{"capacity":100},
    #     "ad3":{"capacity":200},
    #     "ad4":{"capacity":200}
    #     }

    disks = marvin_nas().get_disks()
    print disks

    for (k,v) in disks.items():
        result = result + ("%s,WD1600XXXX-7A,%s\n" % (k,v['capacity']))

    #result = text2html(result)
    return HttpResponse(result)
    # disks = 'No, Type, Size\n'
    # disks = disks + 'Disk1,WD1600XXXX-7A,100GB\n'
    # disks = disks + 'Disk2,WD1600XXXX-7A,300GB\n'
    # disks = disks + 'Disk3,WD1600XXXX-7A,200GB\n'
    # return HttpResponse(disks)

def pool_status(request):
    result = notifier().zpool_status()
    #result = text2html(result)
    return HttpResponse(result)

def pool_status(request):
    result = notifier().zpool_status()
    #result = text2html(result)
    return HttpResponse(result)

def wizard(request):

    logger.info('wizard request!')

    if request.method == 'POST':
        result = ""

        if request.POST["volume_name"] == "":
            result = "Thel volume name cannot be empty!"
            return HttpResponse(result)

        if (len(ZPool.objects.filter(volume_name=request.POST["volume_name"])) !=0 ):
            result = "Thel volume has existed!"
            return HttpResponse(result)

        if (not request.POST.has_key("volume_disks")):
            result = "Please choose disks!"
            return HttpResponse(result)

        volume_disks = request.POST.getlist("volume_disks")

        logger.info(volume_disks)

        # zpool  = ZPool(volume_name = request.POST["volume_name"])
        # zpool.save()

        result = "OK"
        return HttpResponse(result)

    context = {}
    context.update(csrf(request))

    disks = [
        {"name":"ad1","capacity":100},
        {"name":"ad3","capacity":400},
        {"name":"ad4","capacity":200},
        ]
    context["disks"] = disks

    return render_to_response('wizard.html',context)
