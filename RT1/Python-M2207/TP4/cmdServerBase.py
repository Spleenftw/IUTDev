#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socketserver,socket

class ClientHandler(socketserver.BaseRequestHandler):
  def recvstr(self,sfd):
    msg=sfd.readline().rstrip()
    print("<=",msg)
    return msg
  def sendstr(self,sfd,out):
    print("=>",out)
    sfd.writelines(out+'\n')
    sfd.flush()
  def handle(self): 
    print("Start client",self.client_address)
    # print(threading.current_thread())
    sfd=self.request.makefile('rw',encoding='utf-8')
    prompt='CMD srv'
    while cmd != 'bye' :
      cmd=input(prompt+"$ ")
      sendstr(sfd,cmd)
      res=recvstr(sfd)
    self.sendstr(sfd,prompt)
    cmd=self.recvstr(sfd)
    out='Commande [{}] inconnue !'.format(cmd)
    self.sendstr(sfd,out)
    print("Close client")

socketserver.TCPServer.allow_reuse_address=True
s=socketserver.ThreadingTCPServer(('0.0.0.0',5678),ClientHandler)
print("Serveur CMD base...")
try:
  s.serve_forever()
except KeyboardInterrupt:
  s.shutdown()
  s.socket.close()