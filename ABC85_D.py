#貪欲法とは･･･
#常に最善の手を選び続ける方法である。
import math
n,h=map(int, input().split())
a=[]
b=[]
for i in range(n):
    x,y=map(int, input().split())
    a.append(x)
    b.append(y)
ans=0
b.sort(reverse=True)
Am=max(a)
for i in range(n):
    if b[i]>=Am:
        h-=b[i]
        ans+=1
    if h<=0:
        break
if h>0:
    ans+=math.ceil(h/Am)
print(ans)
