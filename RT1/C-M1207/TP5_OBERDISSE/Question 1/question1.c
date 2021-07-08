#include <stdio.h>

//afficher
void afficher (char *str)
{
    int i=0;
    while(str[i]!=0)
    { 
        printf("%c",str[i]);
        i=i+1;
    }
    printf("\n");
}

//longueur
int longueur(char *str)
{
    int i=0;
    while(str[i]!=0)
    {
        i=i+1;
    }
    return i;
}

//recopie
void recopie(char *src,char *dst)
{
    int i=0;
    while(src[i]!=0)
    {
        dst[i]=src[i];
        i=i+1;
    }
    dst[i]=0;
}
//recopie à l'envers
void recopieALenvers(char *str)
    {
    int i=4;
    while(str[i]!=0)
    { 
        printf("%c",str[i]);
        i=i-1;
    }
    printf("\n");
}


//concatene
void concatene (char *str1,char *str2, char *str3)
 {
     int i=0;
     while (str1[i]!=0)
{str3[i]=str1[i];
i++;
}
    int j=0;
    while (str2[j]!=0) {
        str3[i]=str2[j];
        i++;
        j++;
    }
    str3[i]=0;
}

//programme principal
int main ()
{
    char str3[10];
    char str1[]="Salut";
    char str2[20];
    str2[0]='X';
    str2[1]='Y';
    str2[2]='Z';
    str2[3]=0;

    //printf("%c\n",str2[2]);


    afficher(str1);
    printf("%d\n",longueur(str1));
    recopieALenvers(str1);
    concatene (str1, str2, str3);
    afficher(str3);

    return 0;
 }