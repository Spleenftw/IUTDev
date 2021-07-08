#include <stdio.h>

// Création de la structure Temps
struct Temps {
    int se;
    int ce;
};

typedef struct Temps T;

T fabriquer_Temps (double se, double ce)
{
        T t;
        t.se=se;
        t.ce=ce;
        return t;
};

void afficheTemps(T t) {

printf("Temps enregistré : %d secondes et %d centièmes ! \n", t.se, t.ce);
}



int main () {

T t;
t.se = 10;
t.ce = 8;

//printf("Temps enregistré : %d secondes et %d centièmes ! \n", t.se, t.ce);

afficheTemps(t);

T t1=fabriquer_Temps(15,32);
afficheTemps(t1);

return 0;

}
