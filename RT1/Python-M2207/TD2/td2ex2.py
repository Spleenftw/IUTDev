import random

g=random.randrange(1,4500,1)
p=random.randrange(1,4500,1)

a=random.randrange(1,4500,1)
b=random.randrange(1,4500,1)

n1=pow(g,a,p)
n2=pow(g,b,p)

print(pow(n2,a,p))
print(pow(n1,b,p))