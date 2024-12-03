#! /usr/bin/python3

import os
import signal
import sys

def traiteSIGUSR2(signal, frame):
    print("FILS: Pong!\n")
    sys.exit(0)

print("Fils: ready!")

signal.pause()


print("FIls: VIent de sortir du handler de signal SIGUSR2")