#!/bin/bash
count=0; while [ "$count" -lt "$2" ]; do echo -n `date +%s`; echo -n ','; uptime | awk '{print $10 $11 $12}'; sleep $1; ((count += 1)); done
