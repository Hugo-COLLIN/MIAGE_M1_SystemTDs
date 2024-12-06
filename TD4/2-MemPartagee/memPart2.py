#! /usr/bin/python3
# -*- coding: utf-8 -*-

import mmap
import posix_ipc

mem = posix_ipc.SharedMemory('/SM1', posix_ipc.O_CREAT)
tailleEnOctet = mem.size
f = mmap.mmap(mem.fd,tailleEnOctet,access=mmap.ACCESS_WRITE)

print ("début de lecture ")

# affiche le string reçu
msg = bytes(f).decode('utf-8')

# enleve les caracteres vides '\0'
msg = msg.strip('\0')
print('message : \"{}\"'.format(msg))
print ("Fin de lecture ")