#!/usr/bin/env python
from marvin_nas import *
import getopt, sys

def main(argv):
    marvin_nas().destroy_zfs_pool(argv[0])
    

if __name__ == "__main__":
    main(sys.argv[1:])
