T=8542 # Nombre de têtes
C=0 # Nombre de coups
while T!=0:
    T=T/2 # Couper les têtes
    C=C+1 # Comptabiliser les coups
    print("Coup d'épée !")
    if T%2!=0 and T!=1: # Impair
        T=(T*3)+1
    if T==1: # Quasi fini
        print(T," tête restante")
        print("Coup d'épée !")
        C=C+1
        T=0
        
    print(T," têtes restantes")
    
print("Hydre tué en ",C, " coups \o/")
# 111 coups pour 8542 têtes
        
        
    
