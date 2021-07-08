#include <stdio.h>

struct donneesVille {
char* name;
int nbhabitant;
double cox;
double coy;
};

typedef struct donneesVille ville;

ville creerville (char* name, int nbhabitant, double cox, double coy)
{
    ville v;
    v.name=name;
    v.nbhabitant=nbhabitant;
    v.cox=cox;
    v.coy=coy;
    return v;
}


void afficheville(ville v){
printf("Nom : %s\nNombre d`habitants : %d\nX = %f\nY = %f\n\n", v.name, v.nbhabitant, v.cox, v.coy);
}

void affichetableau(ville *tableau, int tailleTableau){
int i;
    for (i = 0 ; i < tailleTableau ; i++){
    afficheville(tableau[i]);
    }
}


int main (int argc, char *argv[]) {
    //ville v;
    //v.name="Béziers";
    //v.nbhabitant=92375;
    //v.cox=55.2;
    //v.coy=98.1;

ville tableauvilles[5];

tableauvilles[0]=creerville("Béziers", 92375, 55.2, 98.1);
tableauvilles[1]=creerville("Montpellier", 290053, 118.9, 144.8);
tableauvilles[2]=creerville("Narbonne", 54700, 49.5, 76.2);
tableauvilles[3]=creerville("Nimes", 149633, 171.3, 133.6);
tableauvilles[4]=creerville("Perpignan", 119188, 25.5, 32.3);

//afficheville(v);
    affichetableau(tableauvilles, 5);
}


