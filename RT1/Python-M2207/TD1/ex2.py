import hashlib
h="396591077b651b11a6c6b712012d4e0fcf1aa817"
# valeur à chercher 3 lettres de 'a' à 'e' + 1 MAJ sans doublons

x="abcde"
for i in x:
   for j in x:
     for k in x:
       if i!=j and i!=k and j!=k:
         maj1=i.upper()+j+k
         maj2=i+j.upper()+k
         maj3=i+j+k.upper()
         h1=hashlib.sha1(bytes(maj1,"utf-8")).hexdigest()
         h2=hashlib.sha1(bytes(maj2,"utf-8")).hexdigest()
         h3=hashlib.sha1(bytes(maj3,"utf-8")).hexdigest()
         if h==h1:
           print("Trouvé :",maj1)
         if h==h2:
           print("Trouvé :",maj2)
         if h==h3:
           print("Trouvé :",maj3)