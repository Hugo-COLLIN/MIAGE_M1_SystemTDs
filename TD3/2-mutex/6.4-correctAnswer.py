#! /usr/bin/python3
# https://www.phind.com/agent?cache=cm4cvsb050002lc0chu77psw7
import threading
import time

mutex1 = threading.Lock()
mutex2 = threading.Lock()
mutex3 = threading.Lock()
count = 0
count_lock = threading.Lock()

class thread_one(threading.Thread):
    def run(self):
        global count
        print("P1: Je suis prêt")
        with count_lock:
            count += 1
            if count == 3:
                mutex1.release()
                mutex2.release()
                mutex3.release()
        mutex1.acquire()
        print("P1: Tu est prêt ?")
        time.sleep(0.1)  # Petit délai pour assurer l'ordre des messages
        print("P1: Merci d'être venu !")
        print("P1: fin")

class thread_two(threading.Thread):
    def run(self):
        global count
        print("P2: Je suis prêt")
        with count_lock:
            count += 1
            if count == 3:
                mutex1.release()
                mutex2.release()
                mutex3.release()
        mutex2.acquire()
        print("P2: Tu est prêt ?")
        time.sleep(0.1)  # Petit délai pour assurer l'ordre des messages
        print("P2: Merci d'être venu !")
        print("P2: fin")

class thread_three(threading.Thread):
    def run(self):
        global count
        print("P3: Je suis prêt")
        with count_lock:
            count += 1
            if count == 3:
                mutex1.release()
                mutex2.release()
                mutex3.release()
        mutex3.acquire()
        print("P3: Tu est prêt ?")
        time.sleep(0.1)  # Petit délai pour assurer l'ordre des messages
        print("P3: Merci d'être venu !")
        print("P3: fin")

# Initialisation des mutex
mutex1.acquire()
mutex2.acquire()
mutex3.acquire()

t1 = thread_one()
t2 = thread_two()
t3 = thread_three()

t1.start()
t2.start()
t3.start()
