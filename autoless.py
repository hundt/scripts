#!/usr/bin/env python
import subprocess
import sys

from fsevents import Observer
from fsevents import Stream

if len(sys.argv) != 2:
    print 'Usage: %s [absolute path to searchfe]' % sys.argv[0]
    sys.exit(1)

observer = Observer()

def callback(args):
    subprocess.call([sys.argv[1] + '/bin/searchfe.sh', 'less'])

stream = Stream(callback, sys.argv[1], file_events=True)
observer.schedule(stream)
observer.run()
