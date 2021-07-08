#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socketserver

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
    msg=self.recvstr(sfd)
    self.sendstr(sfd,msg)
    print("Close client")

socketserver.TCPServer.allow_reuse_address=True
s=socketserver.ThreadingTCPServer(('0.0.0.0',1235),ClientHandler)
print("Serveur d'ECHO...")
try:
  s.serve_forever()
except KeyboardInterrupt:
  s.shutdown()
  s.socket.close()
