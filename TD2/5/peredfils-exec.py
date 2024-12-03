#! /usr/bin/python3
#! -*- coding: utf-8 -*-
import os
import sys

print(sys.argv)
print("PERE: debut prog")
f1pid = os.fork()

if f1pid == 0:
    os.execl("./fils1.py", "a")
else:
    f2pid = os.fork()
    if f2pid == 0:
        os.execl("./fils2.py", "a")
    else:
        pids = (os.getpid(), f1pid, f2pid)
        print("PID-PERE: %d, PID-fils1: %d, PID-fils2: %d" % pids)
        os.waitpid(f1pid, 0)
        print("PERE: mon fils 1 est terminé")
