import math
h,w=map(int,input().split())
mod=10**9+7
a=math.factorial(h+w-2)%mod
b=pow(math.factorial(h-1),mod-2,mod)%mod
c=pow(math.factorial(w-1),mod-2,mod)%mod
print(a*b*c%mod)
