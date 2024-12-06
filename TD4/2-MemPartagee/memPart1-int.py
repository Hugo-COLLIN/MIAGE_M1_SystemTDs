#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import mmap
import posix_ipc as pos
import struct

# affiche le contenu de la mémoire sous forme hexadécimale
def showMem(f, taille):
    print("Contenu de la mémoire :")
    # Convertir en bytes et afficher chaque octet en hexadécimal
    strmem = bytes(f)
    for c in range(taille):
        print('[{:02x}]'.format(strmem[c]), end="")
    print()  # Nouvelle ligne à la fin

tailleMemEnOctet = 64

mem = None
try:
    mem = pos.SharedMemory('/SM1', pos.O_CREAT|pos.O_EXCL, size=tailleMemEnOctet)
except pos.ExistentialError:
    print("La mémoire '/SM1' existe déjà")
    mem = pos.SharedMemory('/SM1', pos.O_CREAT, size=tailleMemEnOctet)
    mem.unlink()
    print("L'instance précédente de '/SM1' a été détruite")
    try:
        mem = pos.SharedMemory('/SM1', pos.O_CREAT|pos.O_EXCL, size=tailleMemEnOctet)
        print("Une nouvelle instance de '/SM1' a été créée")
    except pos.ExistentialError:
        print("Erreur : la mémoire '/SM1' ne peut pas être utilisée.\n fin de programme")
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

# Nombre entier à échanger
msg_int = 10000
print("\nDébut d'écriture des données ")
f.seek(0) # revient à la position 0

# Conversion de l'entier en tableau d'octets
tab_octet = struct.pack(">i", msg_int)
f.write(tab_octet)

# afficher le contenu de la mémoire
showMem(f, tailleMemEnOctet)
print("\nFin d'écriture")