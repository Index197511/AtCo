n,k=map(int,input().split())
a=list(map(int,input().split()))
b=[]
kind=set(a)
c=len(kind)
ans=0
if len(kind)<=k:
    print(0)
elif len(kind)==n:
    print(k)
else:
    for i in kind:
        b.append(a.count(i))
    b.sort()
    for i in range(c-k):
        ans+=b[i]
    print(ans)
