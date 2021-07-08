m=0
n=str(m)
tab=[]
while m<=100:
   print(m,n)
   if m<10:
       A=n[0]
       if m==4*int(A):
           tab.append(n)
   if 10<=m<100:
         A=n[0]
         B=n[1]
         if m==4*int(A)*int(B):
             tab.append(n)
   if m>=100:
        A=n[0]
        B=n[1]
        C=n[2]
        if m==4*int(A)*int(B)*int(C):
            tab.append(n)
   m=m+1
   
