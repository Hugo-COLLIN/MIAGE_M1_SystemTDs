#! /usr/bin/python3

import os
import time
import signal

newpid = os.fork()

if newpid == 0:
    print("FILS: je viens d'être créé")
    os.execl("./pongfils.py", "a")

else:
    print("PERE: j'envoie signal au proc fils ds 10sec")
    time.sleep(10)
    os.kill(newpid, signal.SIGUSR2)

    print("PERE: j'attends le proc fils \n")
    os.wait()
    print("PERE: le processus fils terminé")