# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext


from middleware.text2html import *
from middleware.marvin_nas import *


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
    return render_to_response('wizard.html')
