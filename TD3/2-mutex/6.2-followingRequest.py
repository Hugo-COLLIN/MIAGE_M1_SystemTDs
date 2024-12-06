#! /usr/bin/python3
# https://www.phind.com/agent?cache=cm4cvsb050002lc0chu77psw7
import threading
import time

sem1 = threading.Semaphore(0)
sem2 = threading.Semaphore(0)
sem3 = threading.Semaphore(0)

class thread_one(threading.Thread):
    def run(self):
        print("P1: Je suis prêt")
        sem1.release()
        sem1.release()
        print("P1: Tu est prêt ?")
        sem2.acquire()
        sem3.acquire()
        print("P1: Merci d'être venu !")
        print("P1: fin")

class thread_two(threading.Thread):
    def run(self):
        print("P2: Je suis prêt")
        sem2.release()
        sem2.release()
        print("P2: Tu est prêt ?")
        sem1.acquire()
        sem3.acquire()
        print("P2: Merci d'être venu !")
        print("P2: fin")

class thread_three(threading.Thread):
    def run(self):
        print("P3: Je suis prêt")
        sem3.release()
        sem3.release()
        print("P3: Tu est prêt ?")
        sem1.acquire()
        sem2.acquire()
        print("P3: Merci d'être venu !")
        print("P3: fin")

t1 = thread_one()
t2 = thread_two()
t3 = thread_three()

t1.start()
t2.start()
t3.start()
