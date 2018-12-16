import math
n,m=map(int,input().split())
if abs(n-m)>1:
    print('0')
else:
    if n==m:
       ans1=math.factorial(n)%(10**9+7)
       ans2=math.factorial(n)%(10**9+7)
       print(ans1*ans2*2%(10**9+7))
    else:
       ans1=math.factorial(n)
       ans2=math.factorial(m)
       print(ans1*ans2%(10**9+7))
