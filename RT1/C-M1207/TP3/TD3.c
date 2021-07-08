TD3 M1207 / Fonctions et structures.


2.a)
Résistance équivalente en série : R1 + R2.
Résistance équivalente en parallèle : (R1*R2) / (R1+R2)

2.b)
doubles

2.c)
double serie(double R1, double R2) {
    Req=R1+R2;
return Req;
}

2.d)

double para(double R1, double R2) {
    double Req;
    Req=((R1*R2)/(R1+R2));
return Req;
}

2.e)

#include <stdio.h>

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

//programme principal

int main ()
{
    double R1=..., R2=..., ..., R7=...;
    double Req1, Req2, Req3;
    Req1=serie(R2,R3);
    Req2=para(R1,Req1);

    Req1=serie(Req2,R4);
    Req2=para(R5,R6);
    Req3=serie(Req1, Req2);
    Req1=para(Req3,R7);



    printf("Résistence équivalent ! %f\n", Req1);

    return 0;
}


// definition de la structure complexe
struc complexe {double re; double im;};

//création du type complexe
typedef struc complexe cplx;

cplx fabriquer_cplx(double reel, double imag)
{
    cplx c;
    c.re=reel;
    c.im=imag;
    return c;
}

void affiche_cplx(cplx c)
{
    printf("complexe : (%f, %f)\n", c.re,c.im)
}

cplx add_cplx (cplx c1, cplx c2)
{
    cplx c3=fabriquer_cplx(c1.re+c2.re,im.re+c2.im);
return c3;
}