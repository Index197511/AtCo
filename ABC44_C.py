n,a=map(int,input().split())
x=list(map(int,input().split()))
b=sum(x)
ans=0
dp=[[0]*(b+1)for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for k in range(i+1,0,-1):
        for v in range(b,x[i]-1,-1):
            dp[k][v]+=dp[k-1][v-x[i]]
for k in range(1,n+1):
    if k*a>b:
        break
    ans+=dp[k][k*a]
print(ans)
