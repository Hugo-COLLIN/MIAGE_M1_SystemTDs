#! /usr/bin/python3
# -*- coding: utf8 -*-

import posix_ipc as pos

print("P2 : bonjour, je suis celui qui reçoit un message")

try:
    filmess = pos.MessageQueue("/queue",pos.O_CREAT)
    print("P2 : création de la file de message ou ouverture si déjà créée")
except pos.ExistentialError:
    S = pos.unlink_message_queue("/queue") # détruit la file
    filmess = pos.MessageQueue("/queue",pos.O_CREAT)# puis redemande la création

message=filmess.receive() # retire le message en tête de file
print("P2 : ça y est j'ai reçu un message")
print("P2 : message le plus prioritaire retiré de la file : '{}'".format(message))
nb = filmess.current_messages
print ("Nombre de messages présent : {}".format(nb))