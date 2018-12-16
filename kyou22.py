n,m=map(int,input().split())
a=m//n
ans=1
for i in range(1,a+1):
    if m%i==0:
        ans=max(ans,i)
print(ans)
