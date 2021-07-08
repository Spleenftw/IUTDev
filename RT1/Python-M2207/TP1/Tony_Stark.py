G=1325 # Nombre limite
N=0    # Compteur
C=0    # Code
while N<G:
    if N%3==0 or N%5==0:
        C=C+N
    N=N+1
print("Le code est : ",C)

# Pour 1325, le code est 408543
