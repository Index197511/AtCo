import math
p=[0 for k in range(100000)]
p[1]=1
for k in range(3,100000,2):
    f=1
    for l in range(2,int(math.sqrt(k))+1):
        if k%l==0:
            f=0
            break
    if f==1:
        p[k]=1
c=[0 for k in range(100000)]
c[3]=1
for k in range(3,100000,2):
    if p[k] and p[(k+1)//2]:
        c[k]=1
for k in range(1,100000):
    c[k]+=c[k-1]
for k in range(int(input())):
    l,r=map(int,input().split())
    print(c[r]-c[l-1])
