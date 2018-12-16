n=int(input())
ro=[{}for i in range(n)]
dis=[-1]*n
for i in range(n-1):
    a,b,c=map(int,input().split())
    ro[a-1][b-1]=c
    ro[b-1][a-1]=c
q,k=map(int,input().split())
dis[k-1]=0
stack=[k-1]
while stack:
    s=stack.pop()
    for i,j in ro[s].items():
        if dis[i] == -1:
            dis[i]=dis[s]+j
            stack.append(i)
for i in range(q):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    print(dis[x]+dis[y])
