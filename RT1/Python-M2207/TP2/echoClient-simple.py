#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,sys
try:
  socket=socket.socket()
  socket.connect(("localhost",1234))
  print("Client ECHO simple")
  msg=b'Hello world'
  socket.send(msg)
  print("=>",msg)
  msg=socket.recv(255)
  print("<=",msg)
  print("Close")
  socket.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)
