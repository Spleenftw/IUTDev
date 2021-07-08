#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socketserver,sys

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
    #msg=self.recvstr(sfd)
    #self.sendstr(sfd,msg)
    self.sendstr(sfd,"Authentification en cours...")
    user=self.recvstr(sfd)
    mdp=self.recvstr(sfd)
    rep=""
    if (user=='tata') and (mdp=='tirlipimpon'):
      rep="OK"
    else:
      rep="mauvais user ou mdp"
    self.sendstr(sfd,rep)

    f=open('users.txt')
    for line in f:
        print(line.strip()) # strip() removes LF
    f.close()


    print("Close client")
    
socketserver.TCPServer.allow_reuse_address=True
port=int(sys.argv[1])
s=socketserver.ThreadingTCPServer(('0.0.0.0',port),ClientHandler)
print("Serveur d'ECHO...")
s.serve_forever()

