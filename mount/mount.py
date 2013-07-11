#!/usr/bin/env python
import os
import sys

def main():
    """
    gives the same output as 'mount' command
    """
    mount_file = '/proc/mounts'
    if os.path.isfile(mount_file):
        try:
            f = open(mount_file, 'r')
        except IOError:
            print 'cannot open', mount_file
        else:
            print f.read()
            f.close()
    else:
        print 'cannot find', mount_file

    return 0
       
if __name__ == '__main__':
    sys.exit(main())

