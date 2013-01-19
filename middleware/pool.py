#!/usr/local/bin/python
from notifier import *

result = notifier().get_disks()
print result
# print '-----------'
# for x in reslut.keys():
#   print x

# #print notifier().sysctl('kern.disks')
# # notifier().init('volume')

# #notifier().zpool_create('test_pool',['ad1','ad3'])

# notifier().zpool_create('p1',['ad1'])
# notifier().zpool_create('p2',['ad3'])


# print notifier().zpool_status()
# #notifier().zpool_destroy('test_pool')
