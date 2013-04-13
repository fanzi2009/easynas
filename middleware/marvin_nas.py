import re
from marvin_exceptions import *
from subprocess import *

class marvin_nas(object):
    def __init__(self, ):
        """
        """

    def __pipeopen(self, command):
        #log.debug("Popen()ing: %s", command)
        print command
        return Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE,shell=True)

    def get_disks(self):
        disks = {
            "ad1":{"capacity":100},
            "ad3":{"capacity":200},
            "ad4":{"capacity":200}
            }
        return disks

    def __system(self, command):
        print command
        return call(command, shell=True)
    #return check_call(command, shell=True)

    def __init__zfs_disk(self,disk):
        cmd = 'dd if=/dev/zero of=%s bs=1m count=1' % disk
        self.__system(cmd)

    def __add_disk_into_pool(self,pool_name, pool_type, gpt_disks):
        if pool_type=='stripe':
            pool_type = ''
        cmd = "zpool create -o autoexpand=on -O aclmode=passthrough -O aclinherit=passthrough -f -m /%s -o altroot=/mnt %s %s %s" % (pool_name,pool_name,pool_type,gpt_disks)
        p = self.__pipeopen(cmd)
        p.communicate()
        if p.returncode !=0:
            raise MiddlewareError("zpool create failed! ")

    def __swapon(self,dev_name):
        cmd =  "swapon %s" % dev_name
        self.__system(cmd)

    def __swapoff(self,dev_name):
        cmd =  "swapoff %s" % dev_name
        self.__system(cmd)

    def __swapoff_all(self):
        cmd =  "swapoff -a"
        self.__system(cmd)

    def create_zfs_pool(self,pool_name,pool_type,disks):
        gpt_disks = []
        self.__swapoff_all()
        for x in disks:
            self.__gpt_labeldisk(x , type = "freebsd-zfs")
            gpt_label = self.__gpt_getlabel(x)
            gpt_disks.append("/dev/gptid/%s" % gpt_label[1])
            #FIXME I don' know how to enumerte all disk when destroy pool
            #self.__swapon("/dev/gptid/%s" % gpt_label[0])

        self.__add_disk_into_pool(pool_name, pool_type, " ".join(gpt_disks))

    def destroy_zfs_pool(self,pool_name):
        cmd = "zpool destroy %s" % (pool_name)
        p = self.__pipeopen(cmd)
        p.communicate()
        if p.returncode !=0:
            raise MiddlewareError("zpool destroy failed! ")

    def create_ufs_pool_SD(self,pool_name,disk):
        """create ufs pool for single disk"""
        self.__gpt_labeldisk(disk , type = "freebsd-ufs")
        gpt_label = self.__gpt_getlabel(disk)
        cmd = "newfs -U -L %s /dev/gptid/%s" % (pool_name, gpt_label[1])
        p = self.__pipeopen(cmd)
        p.communicate()
        if p.returncode !=0:
            raise MiddlewareError("UFS create failed! ")


    def create_ufs_pool(self,pool_name,pool_type,disks):
        gpt_disks = []
        self.__swapoff_all()
        if len(disks)==1:
            return self.create_ufs_pool_SD(pool_name,disks[0])
        #newfs -U -L UFSSD /dev/da0p2

        # for x in disks:
        #     self.__gpt_labeldisk(x , type = "freebsd-ufs")
        #     gpt_label = self.__gpt_getlabel(x)
        #     gpt_disks.append("/dev/gptid/%s" % gpt_label[1])
        #     #FIXME I don' know how to enumerte all disk when destroy pool
        #     #self.__swapon("/dev/gptid/%s" % gpt_label[0])

        # self.__add_disk_into_pool(pool_name, pool_type, " ".join(gpt_disks))


    def __gpt_getlabel(self, devname):
        p =self.__pipeopen("gpart list %s" % (devname, ))
        retstring = p.communicate()[0]
        m = re.match(r".+rawuuid:\s+(\w+.\w+.\w+.\w+.\w+)\W.+rawuuid:\s+(\w+.\w+.\w+.\w+.\w+)\W",retstring,re.DOTALL|re.MULTILINE)
        return [m.group(1),m.group(2)]

    def __gpt_labeldisk(self, devname, type, swapsize=2):
        """Label the whole disk with GPT under the desired label and type"""

        # Calculate swap size.
        swapgb = swapsize
        swapsize = swapsize * 1024 * 1024 * 2
        # Round up to nearest whole integral multiple of 128 and subtract by 34
        # so next partition starts at mutiple of 128.
        swapsize = ((swapsize+127)/128)*128
        # To be safe, wipe out the disk, both ends... before we start
        self.__system("dd if=/dev/zero of=/dev/%s bs=1m count=1" % (devname, ))
        try:
            p1 = self.__pipeopen("diskinfo %s" % (devname, ))
            size = int(re.sub(r'\s+', ' ', p1.communicate()[0]).split()[2]) / (1024)
            print size
        except :
            #log.error("Unable to determine size of %s", devname)
            print ("Unable to determine size of %s" % devname)
        else:
            # The GPT header takes about 34KB + alignment, round it to 100
            if size - 100 <= swapgb * 1024 * 1024:
                raise MiddlewareError('Your disk size must be higher than %dGB' % (swapgb, ))
            # HACK: force the wipe at the end of the disk to always succeed. This
            # is a lame workaround.
            self.__system("dd if=/dev/zero of=/dev/%s bs=1m oseek=%s" % (
                devname,
                size / 1024 - 4,
                ))

        commands = []
        commands.append("gpart create -s gpt /dev/%s" % (devname, ))
        if swapsize > 0:
            commands.append("gpart add -b 128 -t freebsd-swap -s %d %s" % (swapsize, devname))
            commands.append("gpart add -t %s %s" % (type, devname))
        else:
            commands.append("gpart add -b 128 -t %s %s" % (type, devname))

        # Install a dummy boot block so system gives meaningful message if booting
        # from the wrong disk.
        #commands.append("gpart bootcode -b /boot/pmbr-datadisk /dev/%s" % (devname))

        for command in commands:
            proc = self.__pipeopen(command)
            print proc.communicate()

            if proc.returncode != 0:
                raise MiddlewareError('Unable to GPT format the disk "%s"' % devname)

        # We might need to sync with reality (e.g. devname -> uuid)
        # Invalidating confxml is required or changes wont be seen
        self.__confxml = None
        # self.sync_disk(devname)

        return
