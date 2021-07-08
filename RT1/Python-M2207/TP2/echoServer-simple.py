#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,sys
try:
  sock=socket.socket()
  sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
  sock.bind(('0.0.0.0',1234))
  print("Serveur d'ECHO simple...")
  sock.listen(5)
  client,address=sock.accept()
  print("Client:",address)
  msg=client.recv(255)
  print("<=",msg)
  client.send(msg)
  print("=>",msg)
  print("Close client")
  client.close()
  print("Bye bye")
  sock.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)
