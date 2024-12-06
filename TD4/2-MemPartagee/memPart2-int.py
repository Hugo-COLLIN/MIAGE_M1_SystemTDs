#! /usr/bin/python3
# -*- coding: utf-8 -*-

import mmap
import posix_ipc
import struct

mem = posix_ipc.SharedMemory('/SM1', posix_ipc.O_CREAT)
tailleEnOctet = mem.size
f = mmap.mmap(mem.fd, tailleEnOctet, access=mmap.ACCESS_WRITE)

print("début de lecture ")
# Lecture du tableau d'octets
msg_octets = bytes(f)[:4]  # On lit les 4 premiers octets (taille d'un entier)

# Conversion du tableau d'octets en entier
msg_int = struct.unpack(">i", msg_octets)[0]
print('message : \"{}\"'.format(msg_int))
print("Fin de lecture ")