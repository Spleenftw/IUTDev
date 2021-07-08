#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,sys

def recvstr(sfd):
  msg=sfd.readline().rstrip()
  print("<=",msg)
  return msg
def sendstr(sfd,out):
  print("=>",out)
  sfd.writelines(out+'\n')
  sfd.flush()
try:
  socket=socket.socket()
  socket.connect(("localhost",1235))
  print("Client ECHO")
  sfd=socket.makefile('rw',encoding='utf-8')
  sendstr(sfd,"Hello world")
  msg=recvstr(sfd)
  print("Close")
  socket.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)
