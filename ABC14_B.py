n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    A=a[i]
    if (x%2)==1:
        ans+=A
    x//=2
print(ans)
