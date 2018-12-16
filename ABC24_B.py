n,t=map(int,input().split())
now=int(input())
ans=t
for i in range(n-1):
    a=int(input())
    if now+t<a:
        ans+=t
        now=a
    else:
        ans+=(a-now)
        now=a

print(ans)
