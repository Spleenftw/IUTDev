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
  ip=sys.argv[1]
  port=int(sys.argv[2])
  message=sys.argv[3]
  socket=socket.socket()
  print(sys.argv[1])
  socket.connect(("localhost",port))
  print("Client ECHO")
  sfd=socket.makefile('rw',encoding='utf-8')
  sendstr(sfd,message)
  a=socket.getsockname()
  b=socket.getpeername()
  print("Addresse source & port source : ",a)
  print("Addresse de destination && port de destination : ",b)
  msg=recvstr(sfd)
  print("Close")
  socket.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)
