#!/usr/bin/env python
import sys
import pwd
import re

def main():
    """
    Get /etc/passwd info and 
    ouput user who can do a proper login
    """

    all_user = pwd.getpwall()
    #print all_user

    notvalid = re.compile('.*/(nologin|false)')
    daemon = re.compile('.*daemon', re.IGNORECASE)
    for user in all_user:
        if not (notvalid.match(user.pw_shell) or \
                daemon.match(user.pw_gecos)):
            print user.pw_name,
    #print [user.pw_name for user in all_user if not notvalid.match(user.pw_shell)]
    #print [user.pw_name for user in all_user if not daemon.match(user.pw_gecos)]

    return 0

if __name__ == '__main__':
    sys.exit(main())
