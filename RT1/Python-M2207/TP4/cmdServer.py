#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socketserver,socket, subprocess, sys

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
    myHostName = socket.gethostname()
    #print("Name of the localhost is {}", format(myHostName))
    prompt=myHostName
    sfd=self.request.makefile('rw',encoding='utf-8')
    self.sendstr(sfd,prompt)
    cmd=''
    while cmd != 'bye':
        cmd=self.recvstr(sfd)
        try:
            res=subprocess.run([cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print('[%s]'%(res.stdout))
        except OSError as err:
            print('Erreur:',err,file=sys.stderr)
        # print(threadi+ng.current_thread())
        if cmd == 'bye':
            out='Commande [{}] Utilisée'.format(cmd)
            self.sendstr(sfd,out)
            print("Close client")
        else:
            out2='Commande [{}] inconnue !'.format(cmd)
            self.sendstr(sfd,out2)
            print("Try again")

socketserver.TCPServer.allow_reuse_address=True
s=socketserver.ThreadingTCPServer(('0.0.0.0',5678),ClientHandler)
print("Serveur CMD base...")
try:
  s.serve_forever()
except KeyboardInterrupt:
  s.shutdown()
  s.socket.close()

