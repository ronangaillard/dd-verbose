#!/usr/local/bin/python

import sys
import signal
from subprocess import Popen, PIPE
import time

dd_process = Popen(['dd'] + sys.argv[1:], stderr=PIPE)

while dd_process.poll() is None:
    dd_process.send_signal(signal.SIGUSR1)
    
    while 1:
        l = dd_process.stderr.readline()
        if 'records in' in l:
            print l[:l.index('+')], 'records',
        if 'bytes' in l:
            print l.strip(), '\r',
            break
        
    time.sleep(.1)
    
print dd_process.stderr.read(),
