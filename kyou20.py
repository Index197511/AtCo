n,t=map(int,input().split())
ans=1000000000
for i in range(n):
    a,b=map(int,input().split())
    if b<=t:
        ans = min(a,ans)
if ans==1000000000:
    print('TLE')
else:
    print(ans)
