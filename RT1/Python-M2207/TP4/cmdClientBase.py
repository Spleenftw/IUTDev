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
  socket.connect(("localhost",5678))
  sfd=socket.makefile('rw',encoding='utf-8')
  print("Client CMD base")
  prompt=recvstr(sfd)
  cmd=''
  while cmd != 'bye' :
    cmd=input(prompt+"$ ")
    #print('commande', [cmd], 'inconnue')
    sendstr(sfd,cmd)
    res=recvstr(sfd)
  print("Close")
  socket.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)
