import itertools
n,k=map(int,input().split())
aa=k/2
a=[]
b=[]
if k%2==0:
    for i in range(1,n+1):
        if i%k==0:
            a.append(i)
        elif i%k==aa:
            b.append(i)
else:
    for i in range(1,n+1):
        if i%k==0:
            a.append(i)
tot=len(set(a))**3+len(set(b))**3
print(tot)
