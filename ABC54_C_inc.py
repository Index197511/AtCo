n,m=map(int,input().split())
g=[[]for i in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
