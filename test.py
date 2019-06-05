l,n=map(int,input().split())
x=[]
ans=0
for i in range(n):
    x.append(int(input()))
now=0
for i in range(n):
    if x[0]-now > now+(l-x[-1]):
        ans+=x[0]-now
        now=x.pop(0)
    else:
        ans+=now+(l-x[-1])
        now=x.pop()
print(ans)
