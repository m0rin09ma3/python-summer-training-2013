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
            lines = []
            lines = f.readlines()
            f.close()

            matching = [line for line in lines if "rootfs" in line]
            #print matching
            
            removed = [lines.remove(m) for m in matching]
            #print removed
            
            for line in lines:
                if line.endswith("0 0\n"):
                    line = line[:-5] 
                    #print line
                    # line = line.rstrip(" 0\n") does not work if
                    # the line contains 0. 
                    # i.e. "...gid=5,mode=620,ptmxmode=000 0 0\n"

                    fields = line.split(" ")
                    #print fields

                    if (len(fields) != 4):
                        print 'cannot format', line
                    else:
                        print fields[0], 'on', fields[1], 'type', fields[2], \
                              '('+ fields[3] + ')'
    else:
        print 'cannot find', mount_file

    return 0
       
if __name__ == '__main__':
    sys.exit(main())

