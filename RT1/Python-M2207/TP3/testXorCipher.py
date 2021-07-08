#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def printValues(txtA,a,txtB,b,txtC,c):
  print('{}: {:>18}'.format(txtA,hex(a)))
  print('{}: {:>18}'.format(txtB,hex(b)))
  print('{}: {:>18}'.format(txtC,hex(c)))

k=0xaeb0e392ed25a496
msg='abcd'
#Transforme msg en entier (big-endian)
m=int.from_bytes(bytes(msg,'utf-8'),byteorder='big')
c=k^m
printValues('M',m,'K',k,'C',c)
#Transforme c en hexadecimal
hexStr=hex(c)

c=int(hexStr,16)
d=k^c
printValues('C',c,'K',k,'D',d)
#Transforme d en séquence de 16 bytes (big-endian)
#et supprime les \x00 en partant de la gauche
y=d.to_bytes(16,byteorder='big').lstrip(b'\x00')
msg=str(y,'utf-8')
print('Msg:',msg)
