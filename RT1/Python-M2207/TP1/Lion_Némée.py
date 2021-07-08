noms=["ARTEMIS", "ASCLEPIOS", "ATHENA", "ATLAS", "CHARON", "CHIRON", "CRONOS", "DEMETER", "EOS", "ERIS", "EROS", "GAIA", "HADES", "HECATE",
"HEPHAISTOS", "HERA", "HERMES", "HESTIA", "HYGIE", "LETO", "MAIA", "METIS", "MNEMOSYNE", "NYX", "OCEANOS", "OURANOS", "PAN", "PERSEPHONE",
"POSEIDON", "RHADAMANTHE", "SELENE", "THEMIS", "THETIS", "TRITON", "ZEUS"]

valeur_mot = 0
valeurs=[]
ordre = []
i = 0
n = 0

for nom in noms:
    while i < len(nom):
        valeur_mot = valeur_mot + ord(nom[i])-64
        i = i + 1
    valeurs.extend([valeur_mot])
    valeur_mot=0
    i=0
print(valeurs)

while len(valeurs) > 0:
	petit = valeurs.index(min(valeurs))
	ordre.append(noms[petit])
	del valeurs[petit]
	del noms[petit]
print(ordre)