def gcd(dis1,dis2):
    if dis2==0:
        return dis1
    else:
        return gcd(dis2,dis1%dis2)
n,x=map(int,input().split())
a=list(map(int,input().split()))
dis=[]
for i in range(n):
    dis.append(abs(a[i]-x))
sort(dis)
if (2,3,5,7,11,13,17,19,23,29,31,37,43,47,53,59,61,67,71,73,79,83,89,97,101) in dis:
    
print(gcd(dis1,dis2))
