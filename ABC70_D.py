from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
n=int(input())
g=[[float('inf') for i in range(n)]for j in range(n)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    g[a-1][b-1]=c
    g[b-1][a-1]=c
q,k=map(int,input().split())
k-=1
cost=dijkstra(g,unweighted=False,directed=False)
for i in range(q):
    a,b=map(int,input().split())
    print(int(cost[a-1][k]+cost[k][b-1]))
