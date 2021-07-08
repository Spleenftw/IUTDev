#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int rand();
    

  srand(time(NULL)); // Initialisation "plus aléatoire" du générateur aléatoire
  for (int i=0;i<10;i++) 
  {
    int x=rand()%101; // Nombre aléatoire entre 0 et 9 inclus
    printf("X: %d\n",x);
 
  }
while (i!=rand())
{
    printf("%d", "&x");
    printf("Saisir la valeur : ");
    scanf("%d", &i);

if (i==rand())
return 1;
}
}


