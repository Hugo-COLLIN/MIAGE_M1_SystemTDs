#! /usr/bin/python3

import posix_ipc as pos

print("P2 : Bonjour")
print("P2 : Création et initialisation des sémaphores")

try:
    S1 = pos.Semaphore("S1",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("P2 : Le sémaphore S1 était déjà créé")
    S1 = pos.Semaphore("S1",pos.O_CREAT)
    print("P2 : La valeur de S1 est {}".format(S1.value))

try:
    S2 = pos.Semaphore("S2",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("P2 : Le sémaphore S2 était déjà créé")
    S2 = pos.Semaphore("S2",pos.O_CREAT)
    print("P2 : La valeur de S2 est {}".format(S2.value))

try:
    S3 = pos.Semaphore("S3",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("P3 : Le sémaphore S3 était déjà créé")
    S3 = pos.Semaphore("S3",pos.O_CREAT)
    print("P3 : S3 value {}".format(S3.value))


print("P2: Je suis prêt")
S2.release()
print("P2: Tu est prêt ?")
S1.acquire()
S3.acquire()
print("P2: Merci d’être venu !")

try:
    S1.unlink()
except pos.ExistentialError:
    print ("P2 : le sémaphore S1 était déjà détruit")

try:
    S2.unlink()
except pos.ExistentialError:
    print ("P2 : le sémaphore S2 était déjà détruit")

try:
    S3.unlink()
except pos.ExistentialError:
    print ("P2 : le sémaphore S3 était déjà détruit")

print ("P2 : fin")