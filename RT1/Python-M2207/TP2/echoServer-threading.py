#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket,sys,threading

class ClientThread(threading.Thread):
  def __init__(self,client,addr):
    threading.Thread.__init__(self)
    self.client=client
    self.addr=addr
    print("[+] Nouveau thread",self.addr)
  def recvstr(self,sfd):
    msg=sfd.readline().rstrip()
    print("<=",msg)
    return msg
  def sendstr(self,sfd,out):
    print("=>",out)
    sfd.writelines(out+'\n')
    sfd.flush()
  def run(self): 
    print("Start client")
    sfd=self.client.makefile('rw',encoding='utf-8')
    msg=self.recvstr(sfd)
    self.sendstr(sfd,msg)
    print("Close client")
    client.close()

try:
  sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
  sock.bind(('0.0.0.0',1235))
  print("Serveur d'ECHO threading...")
  while True:
    sock.listen(5)
    (client,addr)=sock.accept()
    thread=ClientThread(client,addr)
    thread.start()
  print("Bye bye")
  sock.close()
except OSError as err:
  print('Erreur:',err,file=sys.stderr)
