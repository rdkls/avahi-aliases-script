#!/usr/bin/env python3
import subprocess

ip = subprocess.check_output("ifconfig ens1f2 | grep 'inet ' | awk '{print $2}'", shell=True).strip().decode('utf8')

with open('/run/avahi-daemon/avahi-aliases', 'r') as f:
    for line in f.readlines():
      hostname = line.strip()
      if hostname:
        if not hostname.endswith('.local'):
            hostname = f'{hostname}.local'
        subprocess.Popen(['avahi-publish', '-a', hostname, '-R', ip])
