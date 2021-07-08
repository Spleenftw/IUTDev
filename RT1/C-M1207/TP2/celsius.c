#include <stdio.h>


int x=0;
int main ()
{
    printf("Valeur en Farenheit a convertir en degrés :");
    scanf("%d", &x);
    x=((x-32)*0.556);
    printf("%d",x);
    printf("\n");
}