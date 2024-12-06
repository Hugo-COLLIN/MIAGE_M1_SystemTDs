#! /usr/bin/python3
# -*- coding: utf8 -*-

import time
import posix_ipc as pos

print("P1 : bonjour, je suis celui qui envoie des messages")
try:
    filmess = pos.MessageQueue("/queue",pos.O_CREAT)
    print("P1 : création de la file de message ou ouverture si déjà créée")
except pos.ExistentialError:
    S = pos.unlink_message_queue("/queue") # détruit la file
    filmess = pos.MessageQueue("/queue",pos.O_CREAT)# puis redemande la création


print("P1 : informations sur la file de message ")
print("*------")
print ('Max capacité de messages : {}'.format(filmess.max_messages))
print ('Max taille de message (en octets) : {}'.format(filmess.max_message_size))
print ('Nombre de messages present : {}'.format(filmess.current_messages))
print("*------")
time.sleep(5)

message = "Bonjour"
filmess.send(message,None,2) # envoie un message de priorité 2

# envoie d'autres messages
n = filmess.max_messages
for i in range(1,filmess.max_messages):
    message = "M{}".format(i)
    filmess.send(message)


print ("P1 : ça y est j'ai envoyé {} messages ".format(filmess.max_messages))