n,m=map(int,input().split())
ans=0
if n>m//2:
    print(m//2)
elif n==m//2:
    print(n)
elif n<m//2:
    ans+=n
    m-=n*2
    ans+=m//4
    print(ans)
