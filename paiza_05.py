import math
n,x=map(int,input().split())
ans=[]
for i in range(n):
    a,b,c,d=map(int,input().split())
    dist=0
    if a>x:
        ans.append(b)
    elif a==x:
        ans.append(b+d)
    else:
        dist=x-a+1
        if x-a==0:
            dist+=1
        dist=math.ceil(dist/c)
        ans.append(b+dist*d)
print("{} {}".format(min(ans),max(ans)))
