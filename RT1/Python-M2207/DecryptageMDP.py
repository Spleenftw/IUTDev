import hashlib
import time
t0=time.process_time()
# Chercher mot de 5 lettres sans MAJS sans doublons

# Mot de passe encodé
mdp="e4ce56240e94e8c20fe555a20a0e2a6df74b47d2"

# Caractères possibles
car="abcdefghijklmnopqrstuvwxyz"
lim=0
for i in car:
    for j in car:
        for k in car:
             for l in car:
                  for m in car:
                         if i!=j and i!=k and i!=l and i!=m and j!=k and j!=l and j!=m and k!=l and k!=m and l!=m:
                             mot1=i+j+k+l+m
                             mot2=j+k+l+m+i
                             mot3=k+l+m+i+j
                             mot4=l+m+i+j+k
                             mot5=m+i+j+k+l
                             mot6=m+l+k+j+i
                             mot7=l+k+j+i+m
                             mot8=k+j+i+m+l
                             mot9=j+i+m+l+k
                             mot10=i+m+l+k+j
                             print(mot1, mot2, mot3, mot4, mot5, mot6, mot7, mot8, mot9, mot10)
                             if lim==2:
                                 break
                                         
                     # Vérification correspondance
                             h1=hashlib.sha1(bytes(mot1,"utf-8")).hexdigest()
                             h2=hashlib.sha1(bytes(mot2,"utf-8")).hexdigest()
                             h3=hashlib.sha1(bytes(mot3,"utf-8")).hexdigest()
                             h4=hashlib.sha1(bytes(mot4,"utf-8")).hexdigest()
                             h5=hashlib.sha1(bytes(mot5,"utf-8")).hexdigest()
                             h6=hashlib.sha1(bytes(mot6,"utf-8")).hexdigest()
                             h7=hashlib.sha1(bytes(mot7,"utf-8")).hexdigest()
                             h8=hashlib.sha1(bytes(mot8,"utf-8")).hexdigest()
                             h9=hashlib.sha1(bytes(mot9,"utf-8")).hexdigest()
                             h10=hashlib.sha1(bytes(mot10,"utf-8")).hexdigest()
        
                    # Si correspondance 
                             if mdp==h1:
                                print("Trouvé : ",mot1)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h2:
                                print("Trouvé : ",mot2)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h3:
                                print("Trouvé : ",mot3)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h4:
                                print("Trouvé : ",mot4)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h5:
                                print("Trouvé : ",mot5)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h6:
                                print("Trouvé : ",mot6)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h7:
                                print("Trouvé : ",mot7)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h8:
                                print("Trouvé : ",mot8)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h9:
                                print("Trouvé : ",mot9)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2
                             if mdp==h10:
                                print("Trouvé : ",mot10)
                                t1=time.process_time()-t0
                                print("Temps écoulé :", t1)
                                lim=2

     
