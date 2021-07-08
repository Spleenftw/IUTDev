#include <stdio.h>
#include <stdlib.h>
#include <time.h>
// Vous devez obtenir toujours la suite de valeurs 3,6,7,5,3,5,6,2,9,1 à chaque exécution
// Si vous décomentez la ligne 8, vous aurez des valeurs toutes différentes à chaque fois !
int main()
{
  //srand(time(NULL));// Initialisation "plus aléatoire" du générateur aléatoire
  for (int i=0;i<10;i++) {
    int x=rand()%10; // Nombre aléatoire entre 0 et 9 inclus
    printf("X: %d\n",x);
  }
  return 0;
}
