S='123456' # Numéro de série
U=S[0:3]
N=S[-3:]
while N!=0:
    U=int(U)*13 
    Z=str(U)    # Chiffre -> Chaîne
    U=Z[-3:]    # 3 derniers chiffres
    N=int(N)-1  
    print(N, Z, U)

print("Il faut couper le fil n°",U)
        
# Pour n° de série 123456, couper le fil 243 
