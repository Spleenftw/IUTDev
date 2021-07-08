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
  socket.connect(("localhost",9876))
  sfd=socket.makefile('rw',encoding='utf-8')
  print("Client TXT File base")
  prompt=recvstr(sfd)
  cmd=input(prompt+"$ ")
  sendstr(sfd,cmd)
  res=recvstr(sfd)
  while True:
    a=int(res)
    b=0
    while b<a:
      res=recvstr(sfd)
      b=b+1
    if cmd=="@bye":
      socket.close
      break
    
    cmd=input(prompt+"$ ")
    sendstr(sfd,cmd)
    res=recvstr(sfd)  

except OSError as err:
  print('Erreur:',err,file=sys.stderr)


      # if cmd=="users.txt":
      #   res1=recvstr(sfd)
      #   res2=recvstr(sfd)
      #   res3=recvstr(sfd)
      #   res4=recvstr(sfd)

      # if cmd=="txtFileClient.py":
      #   res=recvstr(sfd)
      #   res1=recvstr(sfd)

      # if cmd=="Hello":
      #   res=recvstr(sfd)
      #   res1=recvstr(sfd)

      # if cmd=="@bye":
      #   print("Au revoir")
      #   socket.close()
      #   break



