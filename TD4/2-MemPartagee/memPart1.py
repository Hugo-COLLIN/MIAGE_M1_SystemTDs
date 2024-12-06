#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import mmap
import posix_ipc as pos

# affiche le contenu de la mémoire
def showMem(f, taille):
    print("Contenu de la mémoire :")
    strmem = bytes(f).decode('utf-8')
    for c in range(taille):
        print('[{}]'.format(strmem[c]), end="")

tailleMemEnOctet = 64

mem = None
try:
    mem = pos.SharedMemory('/SM1', pos.O_CREAT|pos.O_EXCL,size=tailleMemEnOctet)
except pos.ExistentialError:
    # Optionnel :
    print("La mémoire '/SM1' existe déjà")
    # Ouverture de la mémoire
    mem = pos.SharedMemory('/SM1', pos.O_CREAT,size=tailleMemEnOctet)
    # Détruction
    mem.unlink()
    print("L'instance précédente de '/SM1' a été détruite")
    # recréeation
    try:
        mem = pos.SharedMemory('/SM1', pos.O_CREAT|pos.O_EXCL,size=tailleMemEnOctet)
        print("Une nouvelle instance de '/SM1' a été créée")
    except pos.ExistentialError:
        print ("Erreur : la mémoire '/SM1' ne peut pas être utilisée.\n fin de programme")
        sys.exit(0)

f = mmap.mmap(mem.fd, tailleMemEnOctet) # pour accéder à la mémoire

tailleMem = mem.size
print("Taille de la mémoire partagée en octet: {}".format(tailleMemEnOctet))

# initialisation de la mémoire
print("Initialisation de la mémoire")
initMem = ''
for i in range(tailleMem):
    initMem += '\0'
f.write(bytes(initMem, encoding='utf-8'))

# afficher le contenu de la mémoire
showMem(f, tailleMemEnOctet)

msg_char_list ="Isaac Asimov"

print("\nDébut d'écriture des données ")
f.seek(0) # revient à la position 0
f.write(bytes(msg_char_list, encoding='utf-8'))

# afficher le contenu de la mémoire
showMem(f, tailleMemEnOctet)
print("\nFin d'écriture")