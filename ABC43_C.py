import math
n=int(input())
a=list(map(int,input().split()))
ave=round(sum(a)/n,0)
ans=0
for i in a:
    ans+=(i-ave)**2
print(int(ans))
