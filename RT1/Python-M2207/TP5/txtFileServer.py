
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
    sfd=self.request.makefile('rw',encoding='utf-8')
    self.sendstr(sfd,'TXT srv')
    fileName=self.recvstr(sfd)
    out='Fichier [{}] inconnu !'.format(fileName)
    self.sendstr(sfd,out)
    print("Close client")

socketserver.TCPServer.allow_reuse_address=True
s=socketserver.ThreadingTCPServer(('0.0.0.0',9876),ClientHandler)
print("Serveur TXT File base...")
try:
  s.serve_forever()
except KeyboardInterrupt:
  s.shutdown()
  s.socket.close()
