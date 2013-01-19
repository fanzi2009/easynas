#!/usr/local/bin/python
from notifier import *
#print notifier().get_disks()

print notifier().sysctl('kern.disks')
