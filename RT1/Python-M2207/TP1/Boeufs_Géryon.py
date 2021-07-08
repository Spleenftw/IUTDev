#!/usr/bin/python3
# -*- coding: utf-8 -*-
B=0     
N=0     
R=0    
y=B*R*N # y=777x aussi
x=B+R+N
z=0
a=0
liste=[]
while z!=1000:
	for B in range(1,1000):
		for N in range(1,1000):
			for R in range(1,1000):
				y=B*R*N
				x=B+R+N
				a=777*x
				if a==y and N<2*B and B<R<N:
					print("Le troupeau contient",x, "boeufs dont ",B, " blancs",R ," roux",N," noirs")
	z=z+1
	break




