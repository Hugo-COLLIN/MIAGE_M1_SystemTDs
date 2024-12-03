#! /usr/bin/python3

import posix_ipc as pos

print("P1 : Bonjour")
print("P1 : Création et initialisation des sémaphores")

try:
    S1 = pos.Semaphore("S1",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("P1 : Le sémaphore S1 était déjà créé")
    S1 = pos.Semaphore("S1",pos.O_CREAT)
    print("P1 : S1 value {}".format(S1.value))

try:
    S2 = pos.Semaphore("S2",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("P1 : Le sémaphore S2 était déjà créé")
    S2 = pos.Semaphore("S2",pos.O_CREAT)
    print("P1 : S2 value {}".format(S2.value))

try:
    S3 = pos.Semaphore("S3",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("P1 : Le sémaphore S3 était déjà créé")
    S3 = pos.Semaphore("S3",pos.O_CREAT)
    print("P1 : S3 value {}".format(S3.value))


print("P1: Je suis prêt")
S1.release()
print("P1: Tu est prêt ?")
S2.acquire()
S3.acquire()
print("P1: Merci d’être venu !")

try:
    S1.unlink()
except pos.ExistentialError:
    print ("P1 : le sémaphore S1 était déjà détruit")

try:
    S2.unlink()
except pos.ExistentialError:
    print ("P1 : le sémaphore S2 était déjà détruit")

try:
    S3.unlink()
except pos.ExistentialError:
    print ("P1 : le sémaphore S3 était déjà détruit")

print ("P1 : fin")