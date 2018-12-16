def gcd(dis1,dis2):
    if dis2==0:
        return dis1
    else:
        return gcd(dis2,dis1%dis2)
n,x=map(int,input().split())
a=list(map(int,input().split()))
dis1=x-min(a)
dis2=max(a)-x
print(gcd(dis1,dis2))
