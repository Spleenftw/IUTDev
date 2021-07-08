import math
import time

a=98765
b=12345
p=123456789876543212345678987654321
start=time.process_time()
x=a**b
end = time.process_time() - start
y=math.log10(x)+1
#print(x)
print('La longueur est de :', len(str(x)),'chiffres')
#print(y)
print('La longueur est de :', x.bit_length(),'bits')
print(end)

print(pow(a, b, p)) #a puissance b modulo p


