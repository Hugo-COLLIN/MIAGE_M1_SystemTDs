#! /usr/bin/python3
#! -*- coding: utf-8 -*-
import os


pid = os.getpid()
print("PERE pid = {}".format(pid))
newpid = os.fork()

# code du fils
if newpid == 0 :
    print("ds fils bjour")
    pidfils = os.getpid()
    print("Dans fils: pid du fils = {}\n".format(pidfils))

    os.execl("./fils1.py", "a")

else:
    #code père
    print("PERE: u  enfant est né\n")
    print("PERE: J'attend le processus fils\n")
    os.wait()
    print("PERE: Le fils a terminé")