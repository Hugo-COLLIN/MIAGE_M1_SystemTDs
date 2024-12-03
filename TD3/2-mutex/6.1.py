#! /usr/bin/python3

import threading, time

mutex1 = threading.Lock()
mutex2 = threading.Lock()

class thread_one(threading.Thread):
    def run(self):
        global mutex1, mutex2
        print("P1: Je suis prêt")
        mutex2.release()
        print("P1: Tu est prêt ?")
        mutex1.acquire()
        print("P1: Merci d'être venu !")

class thread_two(threading.Thread):
    def run(self):
        global mutex1, mutex2
        print("P2: Je suis prêt")
        mutex2.acquire()
        print("P2: Tu est prêt ?")
        time.sleep(5)
        mutex1.release()
        print("P2: Merci d\'être venu !")

mutex1.acquire()
mutex2.acquire()
t1 = thread_one()
t2 = thread_two()
t1.start()
t2.start()