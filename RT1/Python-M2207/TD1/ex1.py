x="abcde" #déclaration de la variable qui va de a à e
cpt=0 #déclaration de la variable compteur
for i in x: #mot d'une seule lettre
	for j in x: #mot de deux lettres
		for k in x: #mot de trois lettres
			if i!=j and i!=k and j!=k: #enlever les doublons
				maj1=i.upper()+j+k #premier mot avec lettre 1 en MAJ
				maj2=i+j.upper()+k #second mot avec lettre 2 en MAJ
				maj3=i+j+k.upper() #troisième mot avec lettre 3 en MAJ
				print(maj1,maj2,maj3) #affichage de toutes les combinaisons
				cpt=cpt+3 #incrémentations du compteur (3 parce que 3 liste de mots)
print(f"Nombre de valeur: {cpt}") #affichage du compteur





#print([i+j for i in x for j in x if x!=j])
#print(len[i+j for i in x for j in x if x!=j])

#print ([i for i in x])
#['a','b','c','d','e']


