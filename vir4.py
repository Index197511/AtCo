q,h,c,d=map(int,input().split())
n=int(input())
c=min(4*q,2*h,c)
if d<2*c:
    if n%2==0:
        print(d*(n//2))
    else:
        print(d*(n//2)+c)
else:
    print(n*c)
