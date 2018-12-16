import sys
import numpy as np
from collections import Counter
s=input()
t=input()
s1=set(s)
t1=set(t)
if s==t:
    print('Yes')
    sys.exit()
qu2=[]
k=0
if len(s1)==len(t1):
    for i in s:
        k+=1
        if s.count(i)>1:
            print(s.count(i))
            qu=[j for j,e in enumerate(s) if e==i]
            for j in qu:
                j=int(j)
                qu2.append(t[j])
            qu3=set(qu2)
            if len(qu3)!=1:
                print('No')
                sys.exit()
            else:
                pass
    qu3.clear()
    qu2=[]
    qu=[]
    print('Yes')
elif len(s1)!=len(t1):
    print('No')
