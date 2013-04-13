#!/usr/bin/env python
from marvin_nas import *
import getopt, sys

def main(argv):
    marvin_nas().create_ufs_pool(argv[0], argv[1], argv[2:])
    
if __name__ == "__main__":
    main(sys.argv[1:])
