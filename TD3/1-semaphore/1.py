#! /usr/bin/python3

import posix_ipc as pos

print("Bonjour")
print("Voici la création et initialisation d'un sémaphore nommé S1")

try:
    S1 = pos.Semaphore("S1",pos.O_CREAT|pos.O_EXCL,initial_value=0)
except pos.ExistentialError:
    print("Le sémaphore S1 était déjà créé.")
    S1 = pos.Semaphore("S1",pos.O_CREAT)
    print("La valeur de S1 est {}".format(S1.value))
    
print ("P1 : fin")