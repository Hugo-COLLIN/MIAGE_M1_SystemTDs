#! /usr/bin/python3
import os
import time

pid = os.getpid()
print("FILS2: un nouveau fils pid = {}".format(pid))
os._exit(0)