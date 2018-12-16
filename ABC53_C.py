import sys
x=int(input())
i=0
cnt=0
cnt+=(x//11)*2
x%=11
if x==0:
    print(cnt)
elif x<=6:
    print(cnt+1)
else:
    print(cnt+2)
