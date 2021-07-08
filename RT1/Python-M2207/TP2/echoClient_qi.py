#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,sys,argparse

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
# i)
  for i,a in enumerate(sys.argv):
    print("Arg({})=>{}".format(i,a))
    if a == "-m":
      message=bytes(sys.argv[i+1], 'utf-8')
    if a == "-p":
      port=int(sys.argv[i+1], base=10)
    if a == "-d":
      dest=sys.argv[i+1]
  socket.connect((str(dest),port))
 
  print("Client ECHO")
  #var1=argparse.ArgumentParser(description='Arguments Client2')
# d)  
  socket.getsockname()
  d=socket.getsockname()
  print("Source :",d)
  socket.getpeername()
  s=socket.getpeername()
  print("Destination :",s)
  sfd=socket.makefile('rw',encoding='utf-8')
# g)
  sendstr(sfd,str(message))
  msg=recvstr(sfd)
  print("Close")
  socket.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)


