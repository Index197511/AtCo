import itertools
from scipy.sparse.csgraph import floyd_warshall
n, m = map(int, input().split())
graph = [[float('inf') for i in range(n)] for i in range(n)]

tmp = []

ans = float('inf')

for i in range(m):
    u, v, l = map(int, input().split())
    if u != 1 and v != 1:
        graph[u-1][v-1] = l
        graph[v-1][u-1] = l
    else:
        tmp.append([u-1, v-1, l])

newgraph = floyd_warshall(csgraph = graph, directed = False)


for i in list(itertools.permutations(tmp, 2)):
    tmp_dist = i[0][2] + newgraph[i[0][1]][i[1][1]] + i[1][2]
    ans = min(ans, tmp_dist)

if ans == float('inf'):
    print(-1)
else:
    print(int(ans))
