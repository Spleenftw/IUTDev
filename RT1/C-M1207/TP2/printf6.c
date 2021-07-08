/*#include <stdio.h>

int tab[6]={5,9,7,3,14,8};
int main()
{
			for ( int x=0 ; x<6 ; x++) 
			{
				for ( int y = tab[x] ; y>0 ; y--) 
				{		
				printf("*");		
				}
			printf("\n");
			}
	return 0;
}

*/


// Les deux marchent. Le premier date de l'année dernière, je sais plus réellement comment j'avais fais.



#include <stdio.h>

int main ()
{
int tab[6]={5,9,7,3,14,8};
int i=1;
int p=0;
	while (i<=6)
	{
		int n=0;
		int t=tab[p];
		while (n<t)
		{
			printf("*");
			n++;
		}
		printf("\n");
		p++;
		i++;
	}
}