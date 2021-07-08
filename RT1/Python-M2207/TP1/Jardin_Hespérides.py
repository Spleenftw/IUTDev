E=1 # Etage
P=0 # Pommes par étage
G=0 # Gain
while E!=51:
    P=E*E 
    print("L'étage ",E," contient ",P," pommes")
    if P%3==0: # Multiple de 3
        G=G+P
    E=E+1
    
print("Hercule pourra emporter ",G," pommes")

# 13464 pommes pour 50 étages
