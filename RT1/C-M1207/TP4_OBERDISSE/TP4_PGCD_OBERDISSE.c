// OBERDISSE Raphaël RT1 B1 2020

#include <stdio.h>
#define MAX 20 // dernier élément du tableau

void initTableau(int *tab, int taille) {
    for(int i=0; i < taille; i++) {
        tab[i] = i+2; 
    }
}

// Question 1.C
void afficherTableau(int *tab, int taille, int afficherZeros) { // 1 = oui, 0 = non
    for(int i=0; i < taille; i++) {
        if(afficherZeros == 1 || tab[i] != 0) {
            printf("%d ", tab[i]);
        }
    }
    printf("\n");
}

// Écrire une fonction qui initialise un tableau (de taille MAX-1) reçu en paramètre en y écrivant tous les nombres de 2 à MAX.
void eratosthene(int *tab, int taille) {
    // question 1.D
    for(int i=0; i < taille; i++) {
        if(tab[i] == 0) continue; 
        int j = i + tab[i];
        while(j < taille) {
            tab[j] = 0; 
            j += tab[i]; 
        }
    }
}

int pgcd(int a, int b) {
    return (b == 0 ||a <= b)? a : (((a%b) == 0) ? b : pgcd(b,a%b));
}

void tester_pgcd(int *tab, int taille) {
    for(int i=0; i < taille; i++) {
        if(tab[i] == 0) continue; // ignore les non-premiers

        int pgcd_res = pgcd(taille, tab[i]);
        printf("pgcd(%d, %d) = %d\n", taille, tab[i], pgcd_res);
    }
}

int main() {
    int taille = MAX-1;
    // question 1.A
    int tab[taille];     
    initTableau(tab, taille);
    // question 1.B
    eratosthene(tab, taille);
    afficherTableau(tab, taille, 0);
    tester_pgcd(tab, taille);

    return 0;
}