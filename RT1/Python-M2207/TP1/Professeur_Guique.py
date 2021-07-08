a=1
b=2
c=5
k=1
n=0
while k<1000-n:
    a=b
    b=c+a
    c=(3*c)+(4*a)-b
    n=a+b
    k=k+1

print("La combinaison du coffre est : ",a,b,c)

# La combinaison du coffre est :  251 829 1909 
    
