#! /usr/bin/python3
import posix_ipc as pos
import sys

print(f"P{sys.argv[1]} : Bonjour")
print(f"P{sys.argv[1]} : Création et initialisation des sémaphores")

try:
    S1 = pos.Semaphore("S1",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print(f"P{sys.argv[1]} : Le sémaphore S1 était déjà créé")
    S1 = pos.Semaphore("S1",pos.O_CREAT)
print(f"P{sys.argv[1]} : S1 value {S1.value}")

try:
    S2 = pos.Semaphore("S2",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print(f"P{sys.argv[1]} : Le sémaphore S2 était déjà créé")
    S2 = pos.Semaphore("S2",pos.O_CREAT)
print(f"P{sys.argv[1]} : S2 value {S2.value}")

try:
    S3 = pos.Semaphore("S3",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print(f"P{sys.argv[1]} : Le sémaphore S3 était déjà créé")
    S3 = pos.Semaphore("S3",pos.O_CREAT)
print(f"P{sys.argv[1]} : S3 value {S3.value}")

print(f"P{sys.argv[1]}: Je suis prêt")

# Logique de synchronisation différente selon le processus
if sys.argv[1] == '1':
    S1.release()
    S1.release()
    print("P1: Tu est prêt ?")
    S2.acquire()
    S3.acquire()
    print("P1: Merci d'être venu !")
elif sys.argv[1] == '2':
    S2.release()
    S2.release()
    print("P2: Tu est prêt ?")
    S1.acquire()
    S3.acquire()
    print("P2: Merci d'être venu !")
elif sys.argv[1] == '3':
    S3.release()
    S3.release()
    print("P3: Tu est prêt ?")
    S1.acquire()
    S2.acquire()
    print("P3: Merci d'être venu !")

# Ne pas détruire les sémaphores à la fin
print(f"P{sys.argv[1]} : fin")