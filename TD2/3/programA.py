#! /usr/bin/python3
import os

print("Prog A")

pid = os.getpid()
print("my pid is {}".format(pid))

os.execl("./programB.py", "a")

print ("Bye A")
