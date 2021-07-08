//OBERDISSE Raphaël RT1 B1.

/*#include <stdio.h>

double Req;

//fonction série

double serie(double R1, double R2) {
    Req=R1+R2;
return Req;
}

//fonction para

double para(double R1, double R2) {
    double Req;
    Req=((R1*R2)/(R1+R2));
return Req;
}

// Programme principal

#include <stdio.h>

int main ()
{
    double R1=100;
    double R2=100;
    double R3=100;
    double R4=100;
    double R5=100;
    double R6=100;
    double R7=100;
    double Req1, Req2, Req3;
    Req1=serie(R2,R3);
    Req2=para(R1,Req1);

    Req1=serie(Req2,R4);
    Req2=para(R5,R6);
    Req3=serie(Req1, Req2);
    Req1=para(Req3,R7);9



    printf("Résistance équivalente : %f\n", Req1);

    return 0;
}
*/



// Deuxième question

/*
#include <stdio.h>

double Req;

//fonction série

double serie(double R1, double R2) {
    Req=R1+R2;
return Req;
}

//fonction para

double para(double R1, double R2) {
    double Req;
    Req=((R1*R2)/(R1+R2));
return Req;
}

// Programme principal
int main ()
{
    double R1=100;
    double R2=R1+100;
    double R3=R2+100;
    double R4=R3+100;
    double R5=R4+100;
    double R6=R5+100;
    double R7=R6+100;
    double Req1, Req2, Req3;
    Req1=serie(R2,R3);
    Req2=para(R1,Req1);

    Req1=serie(Req2,R4);
    Req2=para(R5,R6);
    Req3=serie(Req1, Req2);
    Req1=para(Req3,R7);



    printf("Résistance équivalente : %f\n", Req1);

    return 0;
}


*/

#include <stdio.h>
#include <math.h>
//on déclare la partie réelle et la partie imaginaire

struct complexe
    {                       
        double re;
        double im;
    };
typedef struct complexe cplx;

//création d'un nombre complexe

cplx fabriquer_cplx (double reel, double imag)
    {
        cplx c;
        c.re=reel;
        c.im=imag;
        return c;
    }

// On affiche le complexe

void affiche_cplx (cplx c)
    {
        printf ("%f %f i\n",c.re,c.im);
    }

// addition des complexes

cplx add_cplx (cplx c1, cplx c2)
    {
        cplx c;
        c.re=c1.re+c2.re;
        c.im=c1.im+c2.im;
        return c;
    }

// Multiplication des complexes

cplx mul_cplx (cplx c1, cplx c2)
    {
        cplx c;
        c.re=c1.re*c2.re-c1.im*c2.im;
        c.im=c1.re*c2.im+c2.re*c1.im;
        return c;
    }

// Soustraction des complexes

cplx sous_cplx (cplx c1, cplx c2)
    {
        cplx c;
        c.re=c1.re-c2.re;
        c.im=c1.im-c2.im;
        return c;
    }

// Division des complexes

cplx div_cplx (cplx c1, cplx c2)
    {
        cplx c;
        c.re=(c1.re*c2.re+c1.im*c2.im)/(c2.re*c2.re+c2.im*c2.im);
        c.im=(c1.im*c2.re-c1.re*c2.im)/(c2.re*c2.re+c2.im*c2.im);
        return c;
    }

int main ()
{
	cplx c1=fabriquer_cplx(4,3); // 4 + 3i
	cplx c2=fabriquer_cplx(5,-2); // 5 - 2i
    cplx c3=fabriquer_cplx(2,-1); // 2 - i
    cplx c4=fabriquer_cplx(-5,3); // -5 +3i
    cplx c5=fabriquer_cplx(1,1); // 1 + i
    cplx c6=fabriquer_cplx(2,-4); // 2 - 4i
    cplx c7=fabriquer_cplx(3,2); // 3 + 2i
    cplx c8=fabriquer_cplx(5,-1); // 5 - i 
    cplx c=div_cplx(sous_cplx(mul_cplx(c1,c2),mul_cplx(c3,c4)),add_cplx(mul_cplx(c5,c6),mul_cplx(c7,c8))); //  [(4+3i)*(5-2i)-(2-i)*(-5+3i)]/[(1+i)*(2-4i)+(3+2i)*(5-i)]
    affiche_cplx(c); // On affiche le résultat
	printf("\n"); // retour à la ligne
    	//return 0; // On vérifie que tout a bien marché.

// On calcule le module
double module;
module=sqrt((c.re*c.re) + (c.im*c.im));

// On calcule les arguments
double argc;
double args;
double arg;
double resultat;
argc=(c.re/module);
args=(c.im/module);
arg=atan(c.im/c.re);
resultat=arg*(180/3.14);
printf("Module :%f\n Argument cosinus (rad) :%f\n Argument sinus (rad) :%f\n Argument en radian :%f\n Argument en degré :%f\n", module, argc, args, arg, resultat);
return 0;

}