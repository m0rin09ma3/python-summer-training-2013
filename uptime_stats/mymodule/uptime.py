#!/usr/bin/env python

import subprocess
import shlex

def Uptime():
    """
    extract 3 uptime avgs - 1, 5, 15 minutes
    """
    pipe = subprocess.Popen(['./mymodule/check_uptime.sh', '30', '20'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=False)
    stdoutdata,stderrdata = pipe.communicate()

    return stdoutdata

if __name__ == '__main__':
    print Uptime()

