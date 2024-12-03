#! /usr/bin/python3

import sys
import signal

def close_prog(signal, frame):
    print("time to close!")
    sys.exit(0)


signal.signal(signal.SIGINT, close_prog)

print("LE prog va boucler")
while True:
    continue
