valeurs = []
a = 0
b = 0
c = 0
d = 0

while a < 10:
    b = 0
    while b < 10:
        c = 0
        while c < 10:
            d = 0
            while d < 10:
                gauche = 4*(a*1000 + b*100 + c*10 + d)
                droite = d*1000 + c*100 + b*10 + a
                if gauche == droite:
                    valeurs.append(gauche//4)
                d = d + 1
            c = c + 1
        b = b + 1
    a = a + 1
print("Voici les valeurs de a, b, c et d:", valeurs)