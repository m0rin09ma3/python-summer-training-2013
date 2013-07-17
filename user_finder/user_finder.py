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
    print [user.pw_name for user in all_user if not notvalid.match(user.pw_shell)]

    return 0

if __name__ == '__main__':
    sys.exit(main())
