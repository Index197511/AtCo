n=int(input())
ar=[]
for i in range(n):
    a,b = map(int,input().split())
    ar.append((a,b))
ans=0
ar.reverse()
for ab in ar:
    a = ab[0]+ans
    b = ab[1]
    if a%b!=0:
        ans+=b*(a//b+1)-a
print(ans)
