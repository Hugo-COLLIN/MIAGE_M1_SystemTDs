#! /usr/bin/python3
import os
import time

pid = os.getpid()
print("FILS1: un nouveau fils pid = {}".format(pid))
print("FILS1: sleep 5s")
time.sleep(5)
print("FILS1: terminé")
os._exit(0)