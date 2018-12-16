import math
n=int(input())
r=[]
sum=0
for i in range(n):
    r.append(int(input()))
r.sort(reverse=True)
for i in range(n):
    if i%2==0:
        sum+=r[i]**2
    else:
        sum-=r[i]**2
print(sum*math.pi)
