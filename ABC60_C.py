n,t=map(int,input().split())
a=list(map(int,input().split()))
ans=t
for i in range(1,n):
    ans+=min(t,a[i]-a[i-1])
print(ans)
