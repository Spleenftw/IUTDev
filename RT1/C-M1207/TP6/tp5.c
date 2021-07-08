#include <stdio.h>
#include <stdlib.h>

int q1 (char *str)
{
	int cpt=0;
	while ( str[cpt]!=0 )
	{
		cpt=cpt+1;
	}
	printf("la longueur de la chaine est %d\n",cpt);
	return 0;
}

void q2 (char *str)
{
	int cpt=0;
	printf("str:");
	while ( str[cpt]!=0 )
	{
		printf(" %d",str[cpt]);
		cpt=cpt+1;
	}
	printf("\n");
}

void q3 (char *str)
{
    int cpt=0;
	int var=0;
	int nb=0;
	while ( str[cpt]!=0 )
	{
		var=str[cpt];
		cpt=cpt+1;
		if (var>64 && var<91)
		{
		    nb=nb+1;
		}
	}
	printf("il y a %d majusucule",nb);
	printf("\n");
}

void q4 (char *str)
{
    int cpt=0;
	int var=0;
	int nb=0;
	while ( str[cpt]!=0 )
	{
		var=str[cpt];
		cpt=cpt+1;
		if (var>96 && var<123)
		{
		    nb=nb+1;
		}
	}
	printf("il y a %d minuscule",nb);
	printf("\n");
}

void q6 (char *str)
{
    int cpt=0;
	int var=0;
	int nb=0;
	while ( str[cpt]!=0 )
	{
		var=str[cpt];
		cpt=cpt+1;
		if (var==65 || var==97)
		{
		    nb=nb+1;
		}
	}
	printf("il y a %d a ou A",nb);
	printf("\n");
}

void q7 (char *str,char *dst,char *letremin)
{
    int cpt=0;
	int var=0;
	int nb=0;
	dst[0]=letremin[0];
	int moi=dst[0];
	while ( str[cpt]!=0 )
	{
		var=str[cpt];
		cpt=cpt+1;
		if (var==moi || var==moi-32)
		{
		    nb=nb+1;
		}
	}
	printf("il y a %d %c",nb,letremin[0]);
	printf("\n");
}

void q9 (char *str,char *cara1,char *cara2)
{
    int cpt=0;
	int var=0;
	int nb=0;
	int moi=cara1[0];
	while ( str[cpt]!=0 )
	{
		var=str[cpt];
		printf("%d ",var);
		cpt=cpt+1;
		if (var==moi)
		{
		    str[cpt]=cara2[0];
		}
	}
	printf("voici le nouveau text: %s",str);
	printf("\n");
}

void recopie(char *src,char *dst)
{
	int cpt=0;
	while (src[cpt]!=0)
	{
		dst[cpt]=src[cpt];
		cpt = cpt+1;
	}
	dst[cpt]=0;
		printf("src :%s ",src);
		printf("dst :%s ",dst);
		printf("\n");
}

void recopieALenvers(char *src,char *dst)
{
	int cpt=0;
	int var=0;
	while (src[cpt]!=0)
	{
		cpt=cpt+1;
	}
	cpt=cpt-1;
	while (cpt!=-1)
	{
		dst[var]=src[cpt];
		cpt=cpt-1;
		var=var+1;
	}
	dst[var]=0;
		printf("src :%s",src);
		printf(" dst :%s",dst);
		printf("\n");
}

void concatene(char *src1,char*src2,char*dst)
{
	int i=0;
	while (src1[i]!=0)
	{
		dst[i]=src1[i];
		i=i+1;
	}
	int j=0;
	while (src2[j]!=0)
	{
		dst[i]=src2[j];
		i=i+1;
		j=j+1;
	}
	dst[i]=0;
	printf(" voici la liste:%s",dst);
	printf("\n");
}


int main()
{
    char str[4]={98,97,99,0}; 
    char src1[5]={'s','u','p','e',0};
	char src2[5]={'r','m','a','n',0};
	char dst[12];
	char *txt1="Rien ne sert de courir ; il faut partir à point.\nLe Lièvre et la Tortue en sont un témoignage.\nGageons, dit celle-ci, que vous n'atteindrez point\nSi tôt que moi ce but. Si tôt ? Êtes-vous sage ?\nRepartit l'Animal léger.";
    char *txt2="La Cigale, ayant chanté\nTout l'été,\nSe trouva fort dépourvue\nQuand la bise fut venue :\nPas un seul petit morceau\nDe mouche ou de vermisseau.\nElle alla crier famine\nChez la Fourmi sa voisine,\nLa priant de lui prêter\nQuelque grain pour subsister\nJusqu'à la saison nouvelle.";
    q1 (str);
    recopie(src1,dst);
    recopieALenvers(src1,dst);
    concatene(src1,src2,dst);
    q2 (src1);
    q3 (txt1);
    q4 (txt1);
    q6 (txt1);
    
    char *letremin[1]={'a',0};
    q7 (txt1,dst,letremin);
    
    char *cara1[1]={'a',0};
    char *cara2[1]={'c',0};
    q9 (txt1,cara1,cara2);
    return 0;
}
